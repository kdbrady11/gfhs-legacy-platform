# GFHS Legacy Alumni Platform

A Django and Wagtail based public website and kiosk platform for the Great Falls High School Legacy Alumni Association.

This project is designed to preserve, honor, and display the history, achievements, alumni, records, and archival materials connected to Great Falls High School.

The platform supports both a public website and a web-based touchscreen kiosk experience using the same admin-managed content system.

---

## Project Purpose

The Great Falls High School Legacy Alumni Association exists to preserve and honor the history, culture, achievements, and legacy of Great Falls High School.

This platform is intended to become a living digital monument for:

- Legacy alumni recognition
- School history
- Historical records
- Yearbooks
- Newspapers
- Photographs
- Athletic history
- Fine arts history
- Community impact stories
- Public kiosk displays
- Donation support

---

## Current Prototype Features

The current version includes:

- Public homepage
- About page
- Donate page
- Legacy Alumni section
- Alumni profile detail pages
- Alumni profile images
- Featured alumni on homepage
- School History section
- Historical event detail pages
- Historical event images
- Archives landing page
- Web-based kiosk home screen
- Kiosk alumni listing
- Kiosk alumni detail pages
- Kiosk history listing
- Kiosk history detail pages
- Kiosk archives screen
- Kiosk idle timeout
- Admin-editable content through Wagtail CMS
- Production bootstrap command for demo deployment
- Admin guide documentation

---

## Architecture Overview

The project uses one shared content system.

**Wagtail Admin CMS**  
↓  
**Django/Wagtail Content Models**  
↓  
**Public Website and Touchscreen Kiosk Interface**

This means selected admins can update content once and display it across both the public website and kiosk.

---

## Tech Stack

- Python
- Django
- Wagtail CMS
- SQLite for local development
- Render for prototype deployment
- Gunicorn for production serving
- WhiteNoise for static files
- GitHub for source control

---

## Main Apps

| App | Purpose |
|---|---|
| home | Homepage and reusable standard pages |
| alumni | Legacy alumni profile system |
| history | School history and archive page models |
| kiosk | Touch-friendly kiosk views and templates |
| search | Default Wagtail search app |

---

## Public Website URLs

| Page | URL |
|---|---|
| Home | / |
| About | /about/ |
| Donate | /donate/ |
| Legacy Alumni | /legacy-alumni/ |
| School History | /history/ |
| Archives | /archives/ |

---

## Kiosk URLs

| Kiosk Page | URL |
|---|---|
| Kiosk Home | /kiosk/ |
| Kiosk Alumni | /kiosk/alumni/ |
| Kiosk Alumni Detail | /kiosk/alumni/example-slug/ |
| Kiosk History | /kiosk/history/ |
| Kiosk History Detail | /kiosk/history/example-slug/ |
| Kiosk Archives | /kiosk/archives/ |

---

## Admin Guide

Admin documentation is available here:

docs/admin-guide.md

The admin guide explains how selected admins can:

- Add alumni profiles
- Add history events
- Upload images
- Feature content on the homepage
- Feature content on the kiosk
- Update the Donate page
- Update the Archives page
- Publish changes correctly

---

## Local Development Setup

### 1. Clone the repository

git clone https://github.com/kdbrady11/gfhs-legacy-platform.git

cd gfhs-legacy-platform

### 2. Create a virtual environment

python3.12 -m venv .venv

### 3. Activate the virtual environment

source .venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Run migrations

python manage.py migrate

### 6. Create a local admin user

python manage.py createsuperuser

### 7. Optional: Bootstrap demo content

python manage.py bootstrap_demo

### 8. Run the development server

python manage.py runserver

Open the site at:

http://127.0.0.1:8000/

Open the admin at:

http://127.0.0.1:8000/admin/

---

## Demo Deployment Notes

The project includes a custom bootstrap command:

python manage.py bootstrap_demo

This command creates demo content for deployment environments where an interactive shell is not available.

It can create:

- Demo admin user if environment variables are set
- About page
- Donate page
- Legacy Alumni page
- Sample alumni profiles
- History page
- Sample history events
- Archives page

Required environment variables for production admin creation:

- DJANGO_SUPERUSER_USERNAME
- DJANGO_SUPERUSER_EMAIL
- DJANGO_SUPERUSER_PASSWORD

---

## Render Deployment

Prototype deployment uses this build command:

pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py bootstrap_demo

Start command:

gunicorn gfhs_legacy.wsgi:application

---

## Current Limitations

This prototype is intentionally focused on proving the architecture and user experience.

Current limitations include:

- Uploaded media is not yet configured for permanent cloud storage.
- SQLite is acceptable for local development but should be replaced with PostgreSQL for production.
- Donation processing is represented as a future secure donation link.
- Archive document upload and PDF browsing are not fully implemented yet.
- Search and filtering are still future enhancements.
- Role-specific admin permissions need further configuration.

---

## Recommended Next Features

Recommended next development priorities:

1. Configure PostgreSQL for production.
2. Configure persistent media storage using S3, Cloudinary, or equivalent.
3. Add archive document upload models.
4. Add archive search and filtering.
5. Add alumni achievement timelines.
6. Add image captions and source or credit fields.
7. Add QR codes for kiosk donation and full public profile links.
8. Improve mobile navigation.
9. Add role-specific admin permissions.
10. Add content review and approval workflow.

---

## Demo Talking Point

This project is not just a website. It is the foundation for a shared historical preservation platform.

The public website, admin dashboard, and kiosk all use the same content system. That means selected admins can update alumni profiles, history events, archive messaging, and donation content from one place without touching code.

The long-term goal is to create a permanent digital monument to Great Falls High School history, legacy, alumni, records, and community impact.