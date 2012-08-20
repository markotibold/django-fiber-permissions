from django.conf.urls import patterns, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


from fiber.rest_api import views
from fiber.admin import FiberAdminPageAdmin
from fiber.models import Page
from fiber.fiber_admin import site
from guardian.shortcuts import get_objects_for_user, assign


# Monkey patching
views.ListView.guardian_permissions = None


# This is where the real monkey patching happens\
class PermissionModelAdmin(FiberAdminPageAdmin):

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        super(PermissionModelAdmin, self).save_model(request, obj, form, change)
        assign('change_page', request.user, obj)

site.unregister(Page)
site.register(Page, PermissionModelAdmin)


def post(self, request, *args, **kwargs):
    response = super(views.ListView, self).post(request, *args, **kwargs)
    for permission in self.guardian_permissions:
        assign(permission, request.user, response.raw_content)  # raw_content is the Model instance
    return response
views.ListView.post = post


def get_queryset_listview(self, *args, **kwargs):
    qs = super(views.PaginatedListView, self).get_queryset(*args, **kwargs)
    qs = qs.filter(id__in=get_objects_for_user(self.request.user, self.guardian_permissions, qs))
    return qs
views.PaginatedListView.get_queryset = get_queryset_listview


def get_queryset_tree_listview(self, *args, **kwargs):
    qs = super(views.TreeListView, self).get_queryset(*args, **kwargs)
    qs = qs.filter(id__in=get_objects_for_user(self.request.user, self.guardian_permissions, qs))
    return qs
views.TreeListView.get_queryset = get_queryset_tree_listview

views.FileListView.guardian_permissions = ('add_file', 'change_file', 'delete_file')
views.ImageListView.guardian_permissions = ('add_image', 'change_image', 'delete_image')


admin.autodiscover()


urlpatterns = patterns('',
    (r'^api/v2/', include('fiber.rest_api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',), }),

    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    (r'', 'fiber.views.page'),
)

