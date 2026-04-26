# GFHS Legacy Alumni Platform Permissions Plan

This document outlines the recommended admin roles and permissions for the Great Falls High School Legacy Alumni Association website and kiosk platform.

The goal is to allow selected association admins to manage content safely without giving every user full administrative control.

---

## Permission Strategy

The platform should follow the principle of least privilege.

That means each admin should only receive the access needed for their role.

For example, a person responsible for uploading yearbooks does not need access to user management, deployment settings, or full site configuration.

---

## Recommended Admin Roles

The recommended roles are:

| Role | Purpose |
|---|---|
| Full Admin | Manages the whole platform, users, settings, and all content |
| Content Editor | Manages general public website content |
| Archive Manager | Manages archive items, files, source details, and preservation metadata |
| Kiosk Content Manager | Reviews and manages kiosk-facing content |
| Read-Only Reviewer | Can review content but should not publish changes |

---

## Full Admin

### Purpose

The Full Admin role is for the primary technical or association administrator.

This role should be limited to a small number of trusted users.

### Recommended Access

Full Admin users can:

- Manage all pages
- Add, edit, publish, unpublish, and delete content
- Manage users and groups
- Upload and manage images
- Upload and manage documents
- Manage homepage content
- Manage About and Donate pages
- Manage Legacy Alumni profiles
- Manage School History events
- Manage Archive items
- Manage kiosk display settings
- Review and correct content issues

### Who Should Have This Role

Examples:

- Primary platform owner
- Technical maintainer
- Association-designated lead administrator

---

## Content Editor

### Purpose

The Content Editor role is for trusted users who help maintain normal website content.

This role should be able to update public-facing text and profiles but should not manage users or system settings.

### Recommended Access

Content Editors can:

- Edit and publish the homepage
- Edit and publish the About page
- Edit and publish the Donate page
- Add and edit Legacy Alumni profiles
- Add and edit School History events
- Upload images
- Review public page content

### Restrictions

Content Editors should not:

- Manage users
- Change permission groups
- Delete major site sections
- Change deployment settings
- Access sensitive internal archive notes unless also assigned Archive Manager responsibilities

---

## Archive Manager

### Purpose

The Archive Manager role is for users responsible for historical materials, documents, scans, yearbooks, newspapers, photographs, programs, and records.

This is one of the most important production roles because archive content may involve permissions, source tracking, and public display review.

### Recommended Access

Archive Managers can:

- Add and edit Archive Item pages
- Upload archive files
- Upload archive thumbnails or preview images
- Add source or donor information
- Add credit lines
- Update digitization status
- Update permission status
- Add physical location or archive reference notes
- Add internal notes
- Mark archive items as public display approved
- Mark archive items as featured on kiosk

### Restrictions

Archive Managers should not:

- Manage users
- Change site settings
- Delete major public sections
- Publish sensitive materials without review if the association requires approval

---

## Kiosk Content Manager

### Purpose

The Kiosk Content Manager role is for users responsible for what appears on the touchscreen kiosk.

Kiosk content should be short, visual, public-safe, and easy to navigate.

### Recommended Access

Kiosk Content Managers can:

- Review alumni profiles for kiosk suitability
- Review history events for kiosk suitability
- Review archive items for kiosk suitability
- Enable or disable Featured on kiosk fields
- Check images for kiosk display quality
- Confirm kiosk pages are appropriate for public viewing

### Restrictions

Kiosk Content Managers should not necessarily have permission to:

- Edit full archive governance information
- Manage users
- Change technical settings
- Delete content

---

## Read-Only Reviewer

### Purpose

The Read-Only Reviewer role is for association members or reviewers who need to inspect content before it is published.

This role supports quality control without allowing accidental changes.

### Recommended Access

Read-Only Reviewers can:

- View draft or submitted content if workflow supports it
- Review names, years, dates, and historical accuracy
- Provide feedback outside the system or through a future workflow

### Restrictions

Read-Only Reviewers should not:

- Publish content
- Delete content
- Upload files
- Change page structure
- Manage users

---

## Recommended Publishing Workflow

For production, important historical content should follow a simple review process.

### Suggested Workflow

1. Content is added by a Content Editor or Archive Manager.
2. Names, dates, categories, and descriptions are reviewed.
3. Images and documents are checked for approval and quality.
4. Archive governance fields are completed when applicable.
5. Content is published by an authorized user.
6. Public and kiosk pages are checked after publishing.

---

## Archive Review Checklist

Before publishing an archive item, confirm:

- Title is clear
- Year is accurate or best-known
- Document type is correct
- Description is appropriate
- Source or donor is recorded
- Credit line is added when needed
- Permission status is reviewed
- Public display approval is checked
- Uploaded file is appropriate for public display
- Image or thumbnail displays correctly
- Kiosk display is appropriate if featured

---

## Alumni Review Checklist

Before publishing a Legacy Alumni profile, confirm:

- Name is spelled correctly
- Graduation year is correct if known
- Category is appropriate
- Summary is concise
- Biography is accurate
- Major achievements are verified
- Legacy statement explains significance
- Image is approved for public display
- Homepage feature status is intentional
- Kiosk feature status is intentional

---

## History Review Checklist

Before publishing a School History event, confirm:

- Event title is clear
- Event year is accurate or best-known
- Category is appropriate
- Summary is concise
- Full story provides useful context
- Image is approved for public display
- Kiosk feature status is intentional

---

## Future Workflow Improvements

Future production versions may add:

- Formal content approval workflow
- Draft review states
- Revision approval
- Email notifications for reviewers
- Public contribution inquiry form
- Audit trail review
- Role-specific dashboard views
- Archive source tracking reports

---

## Implementation Notes

Wagtail supports groups and page permissions.

The first production implementation should create these groups:

- Full Admin
- Content Editor
- Archive Manager
- Kiosk Content Manager
- Read-Only Reviewer

Permissions should be tested with sample accounts before handing access to real association users.

The safest first release should keep user management limited to Full Admin users only.