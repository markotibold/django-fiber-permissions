from guardian.shortcuts import get_objects_for_user, get_perms, assign

from fiber.permissions import Permissions


PAGE_PERMISSIONS = ('change_page', 'delete_page')
CONTENTITEM_PERMISSIONS = ('change_contentitem', 'delete_contentitem')


class CustomPermissions(Permissions):
    def filter_objects(self, user, qs):
        if user.is_superuser:
            return qs
        qs = qs.filter(id__in=get_objects_for_user(user, 'change_%s' % qs.model.__name__.lower(), qs.model))
        return qs

    def can_edit(self, user, obj):
        can = 'change_%s' % obj.__class__.__name__.lower() in get_perms(user, obj)
        return can

    def can_move_page(self, user, page):
        return 'change_page' in get_perms(user, page)

    def filter_content_items(self, user, qs):
        if user.is_superuser:
            return qs
        return qs.filter(id__in=get_objects_for_user(user, CONTENTITEM_PERMISSIONS, qs))

    def object_created(self, user, obj):
        assign('change_%s' % obj.__class__.__name__.lower(), user, obj)


# Todo merge with fiber Permissions class
