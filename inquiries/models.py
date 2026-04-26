from django.db import models


class ContributionInquiry(models.Model):
    MATERIAL_TYPE_CHOICES = [
        ("yearbook", "Yearbook"),
        ("newspaper", "Newspaper"),
        ("photo", "Photo"),
        ("program", "Program"),
        ("athletic_record", "Athletic Record"),
        ("fine_arts", "Fine Arts Material"),
        ("general_document", "General Document"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("new", "New"),
        ("reviewing", "Reviewing"),
        ("followed_up", "Followed Up"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
        ("archived", "Archived"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)

    material_type = models.CharField(
        max_length=100,
        choices=MATERIAL_TYPE_CHOICES,
        default="other",
    )

    material_year = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Approximate year of the material, if known.",
    )

    title_or_description = models.CharField(
        max_length=255,
        help_text="Short title or description of the material.",
    )

    details = models.TextField(
        help_text="Additional context, condition, names, dates, or historical relevance.",
    )

    permission_acknowledged = models.BooleanField(
        default=False,
        help_text="Visitor confirms they understand the association must review materials before public display.",
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="new",
    )

    internal_notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contribution Inquiry"
        verbose_name_plural = "Contribution Inquiries"

    def __str__(self):
        return f"{self.name} - {self.get_material_type_display()} - {self.title_or_description}"