from django.shortcuts import get_object_or_404, render

from alumni.models import AlumniDetailPage
from history.models import ArchiveItemPage, HistoricalEventPage


def kiosk_home(request):
    featured_alumni = (
        AlumniDetailPage.objects.live()
        .public()
        .filter(featured_on_kiosk=True)
        .order_by("last_name", "first_name")[:6]
    )

    featured_events = (
        HistoricalEventPage.objects.live()
        .public()
        .filter(featured_on_kiosk=True)
        .order_by("event_year")[:6]
    )

    return render(
        request,
        "kiosk/kiosk_home.html",
        {
            "featured_alumni": featured_alumni,
            "featured_events": featured_events,
        },
    )


def kiosk_alumni(request):
    alumni = (
        AlumniDetailPage.objects.live()
        .public()
        .order_by("last_name", "first_name")
    )

    return render(
        request,
        "kiosk/kiosk_alumni.html",
        {
            "alumni": alumni,
        },
    )


def kiosk_alumni_detail(request, slug):
    alum = get_object_or_404(
        AlumniDetailPage.objects.live().public(),
        slug=slug,
    )

    return render(
        request,
        "kiosk/kiosk_alumni_detail.html",
        {
            "alum": alum,
        },
    )


def kiosk_history(request):
    events = (
        HistoricalEventPage.objects.live()
        .public()
        .order_by("event_year")
    )

    return render(
        request,
        "kiosk/kiosk_history.html",
        {
            "events": events,
        },
    )


def kiosk_history_detail(request, slug):
    event = get_object_or_404(
        HistoricalEventPage.objects.live().public(),
        slug=slug,
    )

    return render(
        request,
        "kiosk/kiosk_history_detail.html",
        {
            "event": event,
        },
    )

def kiosk_archives(request):
    archive_categories = [
        {
            "title": "Yearbooks",
            "description": "Future home for digitized yearbooks, class records, senior sections, and school memories.",
        },
        {
            "title": "Newspapers",
            "description": "Preserve student newspapers, clippings, publications, and stories from across generations.",
        },
        {
            "title": "Photos and Documents",
            "description": "Organize photographs, programs, letters, records, and other historical materials.",
        },
        {
            "title": "Athletic Records",
            "description": "Highlight teams, seasons, records, championships, all-state athletes, and athletic milestones.",
        },
        {
            "title": "Programs and Events",
            "description": "Preserve graduation programs, event materials, fine arts programs, and school celebrations.",
        },
        {
            "title": "Support the Archive",
            "description": "Help digitize, organize, and protect the historical materials that tell the story of Great Falls High School.",
        },
    ]

    featured_archive_items = (
        ArchiveItemPage.objects.live()
        .public()
        .filter(featured_on_kiosk=True)
        .order_by("-archive_year", "title")[:6]
    )

    return render(
        request,
        "kiosk/kiosk_archives.html",
        {
            "archive_categories": archive_categories,
            "featured_archive_items": featured_archive_items,
        },
    )

def kiosk_archive_detail(request, slug):
    archive_item = get_object_or_404(
        ArchiveItemPage.objects.live().public(),
        slug=slug,
    )

    return render(
        request,
        "kiosk/kiosk_archive_detail.html",
        {
            "archive_item": archive_item,
        },
    )

def kiosk_support(request):
    return render(request, "kiosk/kiosk_support.html")