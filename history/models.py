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
            ],
            heading="Historical Event Details",
        ),
        FieldPanel("short_summary"),
        FieldPanel("full_story"),
        FieldPanel("featured_on_kiosk"),
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

    subpage_types = []