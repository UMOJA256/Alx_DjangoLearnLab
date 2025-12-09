# Advanced Features and Security - Django Project

## Custom User Model
- Created `CustomUser` extending `AbstractUser`
- Added fields:
  - `date_of_birth`
  - `profile_photo`
- Updated `settings.py` with `AUTH_USER_MODEL = 'bookshelf.CustomUser'`
- Integrated into Django admin with `CustomUserAdmin`

## Permissions and Groups
- Added custom permissions to `Book` model:
  - `can_create`, `can_edit`, `can_delete`, `can_view`
- Created user groups:
  - Editors, Viewers, Admins
- Enforced permissions in views using `@permission_required` decorator

## Security Best Practices
- `DEBUG = False` in production
- HTTPS enforced with `SECURE_SSL_REDIRECT = True`
- HSTS configured with `SECURE_HSTS_SECONDS = 31536000`
- Cookies secured with `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`
- XSS and content type protections:
  - `SECURE_BROWSER_XSS_FILTER = True`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `X_FRAME_OPTIONS = "DENY"`

## Notes
- All forms use `{% csrf_token %}` for CSRF protection
- ORM used for database queries to prevent SQL injection
# Advanced Features and Security - Django Project

## Custom User Model
- Created `CustomUser` extending `AbstractUser`
- Added fields:
  - `date_of_birth`
  - `profile_photo`
- Updated `settings.py` with `AUTH_USER_MODEL = 'bookshelf.CustomUser'`
- Integrated into Django admin with `CustomUserAdmin`

## Permissions and Groups
- Added custom permissions to `Book` model:
  - `can_create`, `can_edit`, `can_delete`, `can_view`
- Created user groups:
  - Editors, Viewers, Admins
- Enforced permissions in views using `@permission_required` decorator

## Security Best Practices
- `DEBUG = False` in production
- HTTPS enforced with `SECURE_SSL_REDIRECT = True`
- HSTS configured with `SECURE_HSTS_SECONDS = 31536000`
- Cookies secured with `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`
- XSS and content type protections:
  - `SECURE_BROWSER_XSS_FILTER = True`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `X_FRAME_OPTIONS = "DENY"`

## Notes
- All forms use `{% csrf_token %}` for CSRF protection
- ORM used for database queries to prevent SQL injection
