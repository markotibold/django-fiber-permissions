from guardian.shortcuts import get_objects_for_user, get_perms

from fiber.permissions import Permissions

PAGE_PERMISSIONS = ('change_page', 'delete_page')
CONTENTITEM_PERMISSIONS = ('change_contentitem', 'delete_contentitem')


class CustomPermissions(Permissions):
    def filter_pages(self, user, qs):
        if user.is_superuser:
            return qs
        return qs.filter(id__in=get_objects_for_user(user, PAGE_PERMISSIONS, qs))

    def can_edit_content_item(self, user, content_item):
        return 'change_contentitem' in get_perms(user, content_item)

    def can_edit_page(self, user, page):
        return 'change_page' in get_perms(user, page)

    def can_move_page(self, user, page):
        return 'change_page' in get_perms(user, page)

    def filter_content_items(self, user, qs):
        if user.is_superuser:
            return qs
        return qs.filter(id__in=get_objects_for_user(user, CONTENTITEM_PERMISSIONS, qs))
