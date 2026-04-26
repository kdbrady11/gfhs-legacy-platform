from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from wagtail.admin.models import Admin
from wagtail.documents.models import Document
from wagtail.images.models import Image
from wagtail.models import Page


class Command(BaseCommand):
    help = "Create recommended admin groups for the GFHS Legacy platform."

    def handle(self, *args, **options):
        self.create_groups()
        self.stdout.write(self.style.SUCCESS("GFHS admin groups setup complete."))

    def get_permission(self, app_label, codename):
        try:
            return Permission.objects.get(
                content_type__app_label=app_label,
                codename=codename,
            )
        except Permission.DoesNotExist:
            self.stdout.write(
                self.style.WARNING(f"Permission not found: {app_label}.{codename}")
            )
            return None

    def add_permissions(self, group, permissions):
        valid_permissions = [permission for permission in permissions if permission]

        if valid_permissions:
            group.permissions.add(*valid_permissions)

    def create_group(self, name):
        group, created = Group.objects.get_or_create(name=name)

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created group: {name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Group already exists: {name}"))

        return group

    def create_groups(self):
        page_ct = ContentType.objects.get_for_model(Page)
        image_ct = ContentType.objects.get_for_model(Image)
        document_ct = ContentType.objects.get_for_model(Document)
        admin_ct = ContentType.objects.get_for_model(Admin)

        access_admin = Permission.objects.filter(
            content_type=admin_ct,
            codename="access_admin",
        ).first()

        page_permissions = Permission.objects.filter(
            content_type=page_ct,
            codename__in=[
                "add_page",
                "change_page",
                "delete_page",
                "publish_page",
                "bulk_delete_page",
                "lock_page",
                "unlock_page",
            ],
        )

        image_permissions = Permission.objects.filter(
            content_type=image_ct,
            codename__in=[
                "add_image",
                "change_image",
                "delete_image",
                "choose_image",
            ],
        )

        document_permissions = Permission.objects.filter(
            content_type=document_ct,
            codename__in=[
                "add_document",
                "change_document",
                "delete_document",
                "choose_document",
            ],
        )

        full_admin = self.create_group("Full Admin")
        content_editor = self.create_group("Content Editor")
        archive_manager = self.create_group("Archive Manager")
        kiosk_content_manager = self.create_group("Kiosk Content Manager")
        read_only_reviewer = self.create_group("Read-Only Reviewer")

        if access_admin:
            full_admin.permissions.add(access_admin)
            content_editor.permissions.add(access_admin)
            archive_manager.permissions.add(access_admin)
            kiosk_content_manager.permissions.add(access_admin)
            read_only_reviewer.permissions.add(access_admin)

        content_editor.permissions.add(*page_permissions)
        content_editor.permissions.add(*image_permissions)
        content_editor.permissions.add(*document_permissions)

        archive_manager.permissions.add(*page_permissions)
        archive_manager.permissions.add(*image_permissions)
        archive_manager.permissions.add(*document_permissions)

        kiosk_content_manager.permissions.add(*page_permissions)
        kiosk_content_manager.permissions.add(*image_permissions)

        self.stdout.write(self.style.SUCCESS("Applied base group permissions."))