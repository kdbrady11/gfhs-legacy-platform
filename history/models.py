from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index


class HistoryIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    subpage_types = [
        "history.HistoricalEventPage",
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["events"] = (
            HistoricalEventPage.objects.live()
            .public()
            .order_by("event_year")
        )
        return context


class HistoricalEventPage(Page):
    event_year = models.PositiveIntegerField()

    primary_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Primary image used on history cards, public detail pages, and kiosk displays.",
    )

    event_category = models.CharField(
        max_length=100,
        choices=[
            ("school", "School History"),
            ("athletics", "Athletics"),
            ("fine_arts", "Fine Arts"),
            ("community", "Community"),
            ("building", "Building and Campus"),
            ("tradition", "Tradition"),
        ],
        default="school",
    )

    short_summary = models.TextField()
    full_story = RichTextField(blank=True)
    featured_on_kiosk = models.BooleanField(default=False)

    search_fields = Page.search_fields + [
        index.SearchField("short_summary"),
        index.SearchField("full_story"),
        index.FilterField("event_year"),
        index.FilterField("event_category"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("event_year"),
                FieldPanel("event_category"),
                FieldPanel("primary_image"),
            ],
            heading="Historical Event Details",
        ),
        MultiFieldPanel(
            [
                FieldPanel("short_summary"),
                FieldPanel("full_story"),
            ],
            heading="Historical Story",
        ),
        MultiFieldPanel(
            [
                FieldPanel("featured_on_kiosk"),
            ],
            heading="Display Options",
        ),
    ]

    parent_page_types = [
        "history.HistoryIndexPage",
    ]

    subpage_types = []


class ArchivesIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    parent_page_types = [
        "home.HomePage",
    ]

    subpage_types = [
        "history.ArchiveItemPage",
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["archive_items"] = (
            ArchiveItemPage.objects.live()
            .public()
            .order_by("-archive_year", "title")
        )
        return context


class ArchiveItemPage(Page):
    archive_year = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Year connected to this archive item, if known.",
    )

    document_type = models.CharField(
        max_length=100,
        choices=[
            ("yearbook", "Yearbook"),
            ("newspaper", "Newspaper"),
            ("photo", "Photo"),
            ("program", "Program"),
            ("athletic_record", "Athletic Record"),
            ("fine_arts", "Fine Arts"),
            ("general_document", "General Document"),
        ],
        default="general_document",
    )

    primary_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Optional thumbnail or preview image for this archive item.",
    )

    archive_file = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Upload the related PDF, scan, program, newspaper, yearbook, or document.",
    )

    short_description = models.TextField(
        help_text="Short description shown on archive cards."
    )

    full_description = RichTextField(
        blank=True,
        help_text="Longer explanation, context, or historical notes about this item.",
    )

    featured_on_kiosk = models.BooleanField(default=False)

    search_fields = Page.search_fields + [
        index.SearchField("short_description"),
        index.SearchField("full_description"),
        index.FilterField("archive_year"),
        index.FilterField("document_type"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("archive_year"),
                FieldPanel("document_type"),
                FieldPanel("primary_image"),
                FieldPanel("archive_file"),
            ],
            heading="Archive Item Details",
        ),
        MultiFieldPanel(
            [
                FieldPanel("short_description"),
                FieldPanel("full_description"),
            ],
            heading="Archive Description",
        ),
        MultiFieldPanel(
            [
                FieldPanel("featured_on_kiosk"),
            ],
            heading="Display Options",
        ),
    ]

    parent_page_types = [
        "history.ArchivesIndexPage",
    ]

    subpage_types = []