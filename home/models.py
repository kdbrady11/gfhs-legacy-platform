from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    hero_title = models.CharField(
        max_length=255,
        default="Preserving the Legacy of Great Falls High School"
    )

    hero_subtitle = models.TextField(
        default="A living digital monument honoring the history, achievements, and people who shaped Great Falls High School."
    )

    mission_statement = RichTextField(
        blank=True,
        default="The Great Falls High School Legacy Alumni Association exists to preserve history, honor distinguished alumni, and celebrate the culture and achievements of a historic school community."
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("mission_statement"),
    ]

    subpage_types = [
        "home.StandardPage",
    ]


class StandardPage(Page):
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    parent_page_types = [
        "home.HomePage",
    ]

    subpage_types = []