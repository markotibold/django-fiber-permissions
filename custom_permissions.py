from guardian.shortcuts import get_objects_for_user

from fiber.permissions import Permissions


class CustomPermissions(Permissions):
    def filter_pages(self, user, qs):
        if user.is_superuser:
            return qs
        return qs.filter(id__in=get_objects_for_user(user, ('change_page', 'delete_page'), qs))

    def can_edit_content_item(self, user, content_item):
        return False

    def can_edit_page(self, user, page):
        return False
