from django.shortcuts import get_object_or_404, render

from alumni.models import AlumniDetailPage
from history.models import HistoricalEventPage


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