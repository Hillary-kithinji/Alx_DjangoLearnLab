# LibraryProject/bookshelf/management/commands/setup_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Define groups and their permissions
        groups = {
            "Editors": ["can_create", "can_edit"],
            "Viewers": ["can_view"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        content_type = ContentType.objects.get_for_model(Book)

        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_name in perms:
                perm = Permission.objects.get(codename=perm_name, content_type=content_type)
                group.permissions.add(perm)
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' setup with permissions"))
