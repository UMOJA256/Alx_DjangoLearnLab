# Social Media API — Alx_DjangoLearnLab/social_media_api

## Overview

This repository contains a Django REST Framework-based Social Media API skeleton with the following features:

* Custom User model (username, bio, profile picture, following/followers)
* Token authentication (DRF TokenAuth)
* User registration and login endpoints
* Posts and Comments with full CRUD (viewsets)
* Likes system for posts
* Follow / unfollow functionality
* Simple feed endpoint (posts from followed users)
* Notifications model (GenericForeignKey) ready for integration

This project is intended as a baseline to expand into a full social network (likes, real-time notifications, media storage, search, pagination, etc).

## Quick start

### 1. Install dependencies

```bash
pip install -r requirements.txt
# or directly
pip install django djangorestframework djangorestframework-authtoken Pillow
```

### 2. Create project & apps (if starting fresh)

```bash
django-admin startproject social_media_api
cd social_media_api
python manage.py startapp accounts
python manage.py startapp posts
python manage.py startapp notifications
```

### 3. Update `settings.py`

* Add `'rest_framework'`, `'rest_framework.authtoken'`, `'accounts'`, `'posts'`, `'notifications'` to `INSTALLED_APPS`.
* Set `AUTH_USER_MODEL = 'accounts.User'`.
* Configure `MEDIA_URL` and `MEDIA_ROOT`.
* Add `REST_FRAMEWORK` token authentication & pagination config.

### 4. Migrations and run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 5. API Endpoints (examples)

* `POST /api/accounts/register/` — register (returns token)
* `POST /api/accounts/login/` — obtain token (`username` + `password`)
* `GET /api/accounts/users/` — list users
* `POST /api/accounts/users/<username>/follow/` — follow
* `POST /api/accounts/users/<username>/unfollow/` — unfollow
* `GET /api/accounts/users/me/` — your profile
* `GET /api/posts/posts/` — list posts (searchable via `?search=...`)
* `POST /api/posts/posts/` — create post (auth required)
* `POST /api/posts/posts/<id>/like/` — like a post
* `GET /api/posts/feed/` — feed from followed users (auth required)

### 6. Testing

Use Postman / HTTPie / cURL to verify endpoints. Example login:

```
curl -X POST http://127.0.0.1:8000/api/accounts/login/ -d "username=alice&password=secret"
```

## Development notes & improvements

* Replace TokenAuth with JWT for stateless auth if needed.
* Add `django-filter` for advanced filtering.
* Use Celery + Redis for async tasks (notifications, emails).
* Configure static/media storage (S3) and set up HTTPS for production.
* Add unit tests (DRF `APITestCase`) and CI.

## File map (key files to check)

* `accounts/models.py` — custom `User`
* `accounts/serializers.py` — registration & user serializers
* `accounts/views.py` — register + `UserViewSet` (follow/unfollow)
* `posts/models.py` — `Post`, `Comment`, `Like`
* `posts/serializers.py`
* `posts/views.py` — `PostViewSet`, `CommentViewSet`, `FeedView`
* `notifications/models.py` — `Notification` model

## License

MIT (or your preferred license)

## Contact

Project owner / author: mugisha25steven@gmail.com
