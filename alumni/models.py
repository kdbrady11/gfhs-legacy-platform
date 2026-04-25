from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index


class AlumniIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    subpage_types = [
        "alumni.AlumniDetailPage",
    ]

    def get_context(self, request):
        context = super().get_context(request)
        alumni_pages = (
            AlumniDetailPage.objects.live()
            .public()
            .order_by("last_name", "first_name")
        )
        context["alumni_pages"] = alumni_pages
        return context


class AlumniDetailPage(Page):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField(null=True, blank=True)

    category = models.CharField(
        max_length=100,
        choices=[
            ("legacy", "Legacy Alumni"),
            ("athletics", "Athletics"),
            ("fine_arts", "Fine Arts"),
            ("community", "Community Impact"),
            ("faculty_staff", "Faculty and Staff"),
        ],
        default="legacy",
    )

    short_summary = models.TextField(
        help_text="Short summary used for cards and kiosk display."
    )

    biography = RichTextField(blank=True)
    major_achievements = RichTextField(blank=True)
    legacy_statement = RichTextField(
        blank=True,
        help_text="Explain why this person matters to the GFHS legacy."
    )

    featured_on_homepage = models.BooleanField(default=False)
    featured_on_kiosk = models.BooleanField(default=False)

    search_fields = Page.search_fields + [
        index.SearchField("first_name"),
        index.SearchField("last_name"),
        index.SearchField("short_summary"),
        index.SearchField("biography"),
        index.SearchField("major_achievements"),
        index.FilterField("graduation_year"),
        index.FilterField("category"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("first_name"),
                FieldPanel("last_name"),
                FieldPanel("graduation_year"),
                FieldPanel("category"),
            ],
            heading="Basic Information",
        ),
        FieldPanel("short_summary"),
        FieldPanel("biography"),
        FieldPanel("major_achievements"),
        FieldPanel("legacy_statement"),
        MultiFieldPanel(
            [
                FieldPanel("featured_on_homepage"),
                FieldPanel("featured_on_kiosk"),
            ],
            heading="Feature Options",
        ),
    ]

    parent_page_types = [
        "alumni.AlumniIndexPage",
    ]

    subpage_types = []

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"