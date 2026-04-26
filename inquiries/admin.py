from django.contrib import admin

from .models import ContributionInquiry


@admin.register(ContributionInquiry)
class ContributionInquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "material_type",
        "material_year",
        "status",
        "created_at",
    )
    list_filter = (
        "material_type",
        "status",
        "permission_acknowledged",
        "created_at",
    )
    search_fields = (
        "name",
        "email",
        "phone",
        "title_or_description",
        "details",
    )
    readonly_fields = (
        "created_at",
    )