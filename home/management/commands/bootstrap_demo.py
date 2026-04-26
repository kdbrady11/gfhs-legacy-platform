import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from wagtail.models import Page

from home.models import HomePage, StandardPage
from alumni.models import AlumniIndexPage, AlumniDetailPage
from history.models import HistoryIndexPage, HistoricalEventPage, ArchivesIndexPage


class Command(BaseCommand):
    help = "Creates a production admin user and demo content for the GFHS Legacy prototype."

    def handle(self, *args, **options):
        self.create_admin_user()
        self.create_demo_pages()
        self.stdout.write(self.style.SUCCESS("GFHS demo bootstrap complete."))

    def create_admin_user(self):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "keaton")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not password:
            self.stdout.write(
                self.style.WARNING(
                    "DJANGO_SUPERUSER_PASSWORD was not set. Skipping admin user creation."
                )
            )
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created admin user: {username}"))
        else:
            changed = False

            if not user.is_staff:
                user.is_staff = True
                changed = True

            if not user.is_superuser:
                user.is_superuser = True
                changed = True

            if changed:
                user.save()

            self.stdout.write(self.style.WARNING(f"Admin user already exists: {username}"))

    def get_home_page(self):
        home_page = HomePage.objects.live().first()

        if home_page:
            return home_page

        root = Page.get_first_root_node()

        home_page = HomePage(
            title="Home",
            slug="home",
            hero_title="Preserving the Legacy of Great Falls High School",
            hero_subtitle="A living digital monument honoring the history, achievements, and people who shaped Great Falls High School.",
            mission_statement="The Great Falls High School Legacy Alumni Association exists to preserve history, honor distinguished alumni, and celebrate the culture and achievements of a historic school community.",
        )

        root.add_child(instance=home_page)
        home_page.save_revision().publish()

        return home_page

    def child_with_slug_exists(self, parent, slug):
        return parent.get_children().filter(slug=slug).exists()

    def publish_page(self, parent, page):
        parent.add_child(instance=page)
        page.save_revision().publish()
        return page

    def create_demo_pages(self):
        home_page = self.get_home_page()

        self.create_standard_page(
            parent=home_page,
            title="About",
            intro="Preserving the history, culture, achievements, and legacy of Great Falls High School.",
            body=(
                "The Great Falls High School Legacy Alumni Association exists to preserve and honor the history, "
                "culture, achievements, and legacy of Great Falls High School. The association recognizes individuals, "
                "teams, traditions, records, and moments that reflect the lasting impact of the school and its community.\n\n"
                "This digital platform is being developed as both a public website and a future touchscreen kiosk experience. "
                "Its purpose is to make the school’s history accessible to alumni, students, families, visitors, and the Great Falls community."
            ),
        )

        self.create_standard_page(
            parent=home_page,
            title="Donate",
            intro="Help preserve the history, records, stories, and legacy of Great Falls High School for future generations.",
            body=(
                "The Great Falls High School Legacy Alumni Association is building a living historical preservation platform "
                "for alumni recognition, school history, archival documents, yearbooks, newspapers, photographs, and future public kiosk displays.\n\n"
                "Donations help support the preservation of historical materials, the digitization of school records, "
                "the recognition of distinguished alumni, and the development of public-facing displays that make this history accessible "
                "to students, alumni, families, and the Great Falls community.\n\n"
                "In the final version, this page can connect to a secure donation provider such as Stripe, while the kiosk can display "
                "a QR code so visitors can donate from their own phone instead of entering payment information on a public touchscreen.\n\n"
                "Secure online donation link coming soon."
            ),
        )

        alumni_index = self.create_alumni_index(home_page)
        self.create_sample_alumni(alumni_index)

        history_index = self.create_history_index(home_page)
        self.create_sample_history_events(history_index)

        self.create_archives_index(home_page)

    def create_standard_page(self, parent, title, intro, body):
        slug = slugify(title)

        if self.child_with_slug_exists(parent, slug):
            self.stdout.write(self.style.WARNING(f"Page already exists: {title}"))
            return

        page = StandardPage(
            title=title,
            slug=slug,
            intro=intro,
            body=body,
        )

        self.publish_page(parent, page)
        self.stdout.write(self.style.SUCCESS(f"Created page: {title}"))

    def create_alumni_index(self, parent):
        slug = "legacy-alumni"

        existing = parent.get_children().filter(slug=slug).first()
        if existing:
            self.stdout.write(self.style.WARNING("Legacy Alumni page already exists."))
            return existing.specific

        page = AlumniIndexPage(
            title="Legacy Alumni",
            slug=slug,
            intro=(
                "The Legacy Alumni section honors individuals connected to Great Falls High School whose accomplishments, "
                "service, leadership, character, or lasting impact represent the school’s proud history."
            ),
        )

        self.publish_page(parent, page)
        self.stdout.write(self.style.SUCCESS("Created page: Legacy Alumni"))
        return page

    def create_sample_alumni(self, parent):
        sample_alumni = [
            {
                "title": "Jane Doe",
                "first_name": "Jane",
                "last_name": "Doe",
                "graduation_year": 1978,
                "category": "legacy",
                "short_summary": "A Great Falls High School graduate recognized for a lifetime of leadership, service, and community impact.",
                "biography": "Jane Doe represents the type of distinguished graduate this platform is designed to honor. Her profile demonstrates how the association can preserve alumni stories, achievements, photographs, and historical context in one shared system.",
                "major_achievements": "Community leadership, professional excellence, public service, and long-term support for education and civic engagement.",
                "legacy_statement": "This profile is placeholder content for the prototype. In the final system, this section will explain why each individual’s story matters to the Great Falls High School legacy.",
                "featured_on_homepage": True,
                "featured_on_kiosk": True,
            },
            {
                "title": "John Smith",
                "first_name": "John",
                "last_name": "Smith",
                "graduation_year": 1985,
                "category": "athletics",
                "short_summary": "A former student athlete whose accomplishments reflect the athletic tradition and competitive spirit of Great Falls High School.",
                "biography": "John Smith is sample content for the prototype alumni section. This profile shows how athletic accomplishments, records, photos, awards, and related history can eventually be preserved.",
                "major_achievements": "Athletic achievement, team leadership, school pride, and continued connection to the Great Falls community.",
                "legacy_statement": "This placeholder profile demonstrates how the kiosk and public website can both display alumni recognition from the same admin-managed content.",
                "featured_on_homepage": False,
                "featured_on_kiosk": True,
            },
        ]

        for alum in sample_alumni:
            slug = slugify(alum["title"])

            if self.child_with_slug_exists(parent, slug):
                self.stdout.write(self.style.WARNING(f"Alumni profile already exists: {alum['title']}"))
                continue

            page = AlumniDetailPage(
                title=alum["title"],
                slug=slug,
                first_name=alum["first_name"],
                last_name=alum["last_name"],
                graduation_year=alum["graduation_year"],
                category=alum["category"],
                short_summary=alum["short_summary"],
                biography=alum["biography"],
                major_achievements=alum["major_achievements"],
                legacy_statement=alum["legacy_statement"],
                featured_on_homepage=alum["featured_on_homepage"],
                featured_on_kiosk=alum["featured_on_kiosk"],
            )

            self.publish_page(parent, page)
            self.stdout.write(self.style.SUCCESS(f"Created alumni profile: {alum['title']}"))

    def create_history_index(self, parent):
        slug = "history"

        existing = parent.get_children().filter(slug=slug).first()
        if existing:
            self.stdout.write(self.style.WARNING("History page already exists."))
            return existing.specific

        page = HistoryIndexPage(
            title="History",
            slug=slug,
            intro=(
                "The School History section preserves the traditions, milestones, achievements, "
                "and defining moments that shaped Great Falls High School across generations."
            ),
        )

        self.publish_page(parent, page)
        self.stdout.write(self.style.SUCCESS("Created page: History"))
        return page

    def create_sample_history_events(self, parent):
        sample_events = [
            {
                "title": "A Tradition of Excellence",
                "event_year": 1900,
                "event_category": "school",
                "short_summary": "A foundational moment representing the long-standing history, pride, and identity of Great Falls High School.",
                "full_story": "This placeholder event represents the type of historical milestone that can be preserved in the final platform. Future versions can include verified dates, photographs, documents, newspaper clippings, and related alumni stories.",
                "featured_on_kiosk": True,
            },
            {
                "title": "Preserving the Legacy",
                "event_year": 2026,
                "event_category": "tradition",
                "short_summary": "The Legacy Alumni Association begins building a digital preservation platform to honor the school’s history and achievements.",
                "full_story": "This prototype demonstrates how Great Falls High School history, alumni recognition, archives, and kiosk displays can be managed from one shared content system.",
                "featured_on_kiosk": True,
            },
        ]

        for event in sample_events:
            slug = slugify(event["title"])

            if self.child_with_slug_exists(parent, slug):
                self.stdout.write(self.style.WARNING(f"Historical event already exists: {event['title']}"))
                continue

            page = HistoricalEventPage(
                title=event["title"],
                slug=slug,
                event_year=event["event_year"],
                event_category=event["event_category"],
                short_summary=event["short_summary"],
                full_story=event["full_story"],
                featured_on_kiosk=event["featured_on_kiosk"],
            )

            self.publish_page(parent, page)
            self.stdout.write(self.style.SUCCESS(f"Created historical event: {event['title']}"))

    def create_archives_index(self, parent):
        slug = "archives"

        if self.child_with_slug_exists(parent, slug):
            self.stdout.write(self.style.WARNING("Archives page already exists."))
            return

        page = ArchivesIndexPage(
            title="Archives",
            slug=slug,
            intro=(
                "The Historical Archives section is designed to preserve and organize the documents, photographs, "
                "yearbooks, newspapers, records, and stories connected to Great Falls High School."
            ),
        )

        self.publish_page(parent, page)
        self.stdout.write(self.style.SUCCESS("Created page: Archives"))