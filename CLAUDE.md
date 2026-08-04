# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Django + Django REST Framework backend for a travel/tourism platform ("Foringer Dol" / CatchBangladesh). Exposes JSON APIs for locations, hotels, events, tours, blogs, reviews, pictures, and bookings, with JWT-based auth. No frontend lives in this repo.

## Setup & commands

- Requires a `.env` file in the project root (read via `django-environ`) with at minimum: `SECRET_KEY`, `DEBUG`, `DB_NAME`, `DB_USER`, `DB_PASS`. The DB is MySQL, hardcoded to host `127.0.0.1:3306` in `foringerDol/settings.py`.
- Install deps: `pip install -r requirements.txt`
- Run dev server: `python manage.py runserver`
- Apply migrations: `python manage.py migrate`
- Create migrations after model changes: `python manage.py makemigrations`
- Run tests (per-app, standard Django test runner — each app has a `tests.py` but they are currently empty stubs): `python manage.py test` or `python manage.py test <app_name>`
- Django admin is enabled at `/admin/`.

## Architecture

**One Django app per domain entity**, each following an identical structure: `models.py`, `serializers.py`, `views.py` (function-based `@api_view` views, not DRF viewsets/generics), `urls.py`, `admin.py`. Apps: `accounts`, `locations`, `hotels`, `events`, `tours`, `blogs`, `reviews`, `pictures`, `booking`.

Each app's `urls.py` is included under a matching prefix in `foringerDol/urls.py` (e.g. `locations/`, `hotels/`, `booking/`).

### Central entity: Location

`locations.Location` is the hub model. `hotels.Hotel`, `events.Event`, `tours.Tour`, and `booking.Booking` all hold a `ForeignKey` to `Location` (`on_delete=CASCADE`). `booking.Booking` additionally FKs to `events.Event`. There is no reverse hub logic beyond standard related-name lookups (e.g. `location.events`, `location.hotel`).

### Auth

- `accounts` app handles registration (`RegisterView`) and issues JWTs via `djangorestframework-simplejwt`. Login/refresh use DRF SimpleJWT's built-in `TokenObtainPairView`/`TokenRefreshView` directly in `accounts/urls.py` — there's no custom login view.
- `REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']` is JWT-only, but most views leave `@permission_classes([IsAuthenticated])` commented out, so many "write" endpoints (create/update) are effectively open while delete/toggle endpoints tend to require auth. Check each view individually — there's no consistent policy.

### View conventions (repeated across every app)

Views are function-based, decorated with `@api_view([...])`, and follow a fixed response envelope:
```python
{'code': status.HTTP_xxx, 'response': "...", 'data': serializer.data}  # or 'error': str(e)
```
Nearly every view wraps its body in a broad `try/except Exception as e`, returning `HTTP_400_BAD_REQUEST` in the except block regardless of the actual failure mode (so HTTP status codes in responses are unreliable — check the `code`/`error` fields in the body instead).

Typical CRUD set per entity: `view_<entity>` (list + detail-by-slug), `create_<entity>`, `complete_update`/`partial_update` (PATCH), `delete_<entity>`. `booking` additionally has `toggle_payment_status`.

### Image uploads

Models with images (`Location`, `Hotel`, `Event`, `Tour`, `Blog`, `Pictures`) use a per-app `generate_filename(instance, filename)` helper that renames uploads to `foring<Entity>_<uuid4>.<ext>` (files land in `media/`, served at `MEDIA_URL`). Create/update views accept images as base64 data URIs in JSON (`"data:<mime>;base64,<data>"`), decoded manually via `base64.b64decode` into a `ContentFile` before handing off to the serializer — there is no multipart/form-data image upload path.

### Slugs

Slugged models (`Location`, `Event`, `Hotel`, `Tour`, `Blog`) generate slugs manually in the view (not via `save()` override or a signal): `slugify(name) + "-" + suffix`, where `suffix` is `1 + count of existing rows with the same name`. This logic is duplicated per-app in `create_*`/`complete_update` views rather than shared.

### CORS / settings notes

- `CORS_ALLOW_ALL_ORIGINS = True` and `ALLOWED_HOSTS = ['*']` — wide open, dev-oriented config.
- `APPEND_SLASH = False`, so URLs must be hit with their exact trailing slash as defined in each `urls.py`.
- `SIMPLE_JWT`: access tokens last 10 days, refresh tokens 1 day (unusually inverted from the typical short-access/long-refresh pattern — be aware when touching auth).
