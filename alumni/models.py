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

        selected_category = request.GET.get("category", "").strip()
        selected_year = request.GET.get("year", "").strip()
        search_query = request.GET.get("q", "").strip()

        category_labels = {
            "legacy": "Legacy Alumni",
            "athletics": "Athletics",
            "fine_arts": "Fine Arts",
            "community": "Community Impact",
            "faculty_staff": "Faculty and Staff",
        }

        alumni_pages = (
            AlumniDetailPage.objects.live()
            .public()
            .order_by("last_name", "first_name")
        )

        if selected_category in category_labels:
            alumni_pages = alumni_pages.filter(category=selected_category)

        if selected_year.isdigit():
            alumni_pages = alumni_pages.filter(graduation_year=int(selected_year))

        if search_query:
            alumni_pages = alumni_pages.filter(
                models.Q(title__icontains=search_query)
                | models.Q(first_name__icontains=search_query)
                | models.Q(last_name__icontains=search_query)
                | models.Q(short_summary__icontains=search_query)
                | models.Q(biography__icontains=search_query)
                | models.Q(major_achievements__icontains=search_query)
                | models.Q(legacy_statement__icontains=search_query)
            )

        available_years = (
            AlumniDetailPage.objects.live()
            .public()
            .exclude(graduation_year__isnull=True)
            .order_by("-graduation_year")
            .values_list("graduation_year", flat=True)
            .distinct()
        )

        context["alumni_pages"] = alumni_pages
        context["selected_category"] = selected_category
        context["selected_category_label"] = category_labels.get(selected_category)
        context["selected_year"] = selected_year
        context["search_query"] = search_query
        context["category_labels"] = category_labels
        context["available_years"] = available_years

        return context


class AlumniDetailPage(Page):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField(null=True, blank=True)

    primary_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Primary photo used on alumni cards, detail pages, homepage features, and kiosk displays.",
    )

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
                FieldPanel("primary_image"),
            ],
            heading="Basic Alumni Information",
        ),
        MultiFieldPanel(
            [
                FieldPanel("short_summary"),
                FieldPanel("biography"),
                FieldPanel("major_achievements"),
                FieldPanel("legacy_statement"),
            ],
            heading="Profile Story and Legacy",
        ),
        MultiFieldPanel(
            [
                FieldPanel("featured_on_homepage"),
                FieldPanel("featured_on_kiosk"),
            ],
            heading="Display Options",
        ),
    ]

    parent_page_types = [
        "alumni.AlumniIndexPage",
    ]

    subpage_types = []

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"