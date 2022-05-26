import os

from configurations import Configuration

from .environment import env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rel(*path):
    """
    Used to get the relative path for any file, combines with the BASEDIR
    @param path: the relative path for the file
    @return: absolute path to the file
    """
    return os.path.join(BASE_DIR, *path)


class Common(Configuration):
    """
    The common settings
    """

    BASE_DIR = BASE_DIR

    SECRET_KEY = env.str(
        "{{ cookiecutter.project_slug | upper() }}_SECRET_KEY", default="temp"
    )

    INSTALLED_APPS = [
        # django apps
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # 3rd party apps
        "rest_framework",
        "rest_framework.authtoken",
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "dj_rest_auth",
        "dj_rest_auth.registration",
        "django_extensions",
        "django_filters",
        "drf_yasg",
        "drf_psq",
        "corsheaders",
        "django_celery_beat",
        "django_celery_results",
        # our apps
        "{{ cookiecutter.project_slug }}.apps.common.apps.CommonConfig",
        "{{ cookiecutter.project_slug }}.apps.accounts.apps.AccountsConfig",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "{{ cookiecutter.project_slug }}.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [rel("templates/")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            },
        }
    ]

    # Static and media files
    STATIC_URL = env.str(
        "{{ cookiecutter.project_slug | upper() }}_STATIC_URL",
        default="/static/",
    )
    STATIC_ROOT = rel("static_collected")
    STATICFILES_DIR = rel("static")

    # Media config
    MEDIA_URL = "/media/"
    MEDIA_ROOT = rel("media")

    AUTH_USER_MODEL = "accounts.User"
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": (
                "django.contrib.auth.password_validation"
                ".UserAttributeSimilarityValidator"
            ),
        },
        {
            "NAME": (
                "django.contrib.auth.password_validation"
                ".MinimumLengthValidator"
            ),
        },
        {
            "NAME": (
                "django.contrib.auth.password_validation"
                ".CommonPasswordValidator"
            ),
        },
        {
            "NAME": (
                "django.contrib.auth.password_validation"
                ".NumericPasswordValidator"
            ),
        },
    ]

    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Logging
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "django.server": {
                "()": "django.utils.log.ServerFormatter",
                "format": "[%(server_time)s] %(message)s",
            },
            "verbose": {
                "format": (
                    "%(levelname)s %(asctime)s "
                    "%(module)s %(process)d %(thread)d %(message)s"
                )
            },
            "simple": {"format": "%(levelname)s %(message)s"},
            "sql": {
                "()": "{{ cookiecutter.project_slug }}.loggers.SQLFormatter",
                "format": "%(duration).3f %(statement)s",
            },
        },
        "filters": {
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            },
        },
        "handlers": {
            "django.server": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "django.server",
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
            },
            "sql": {
                "class": "logging.StreamHandler",
                "formatter": "sql",
                "level": "DEBUG",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "propagate": True,
            },
            "django.server": {
                "handlers": ["django.server"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["mail_admins", "console"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["console", "sql"],
                "level": "INFO",
            },
        },
    }

    SECURE_BROWSER_XSS_FILTER = env.bool(
        "{{ cookiecutter.project_slug | upper() }}_SECURE_BROWSER_XSS_FILTER",
        default=True,
    )
    SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
        "{{ cookiecutter.project_slug | upper() }}_SECURE_CONTENT_TYPE_NOSNIFF",
        default=True,
    )
    SESSION_COOKIE_HTTPONLY = env.bool(
        "{{ cookiecutter.project_slug | upper() }}_SESSION_COOKIE_HTTPONLY",
        default=True,
    )
    SESSION_COOKIE_SECURE = env.bool(
        "{{ cookiecutter.project_slug | upper() }}_SESSION_COOKIE_SECURE",
        default=True,
    )
    CSRF_COOKIE_SECURE = env.bool(
        "{{ cookiecutter.project_slug | upper() }}_CSRF_COOKIE_SECURE",
        default=True,
    )
    X_FRAME_OPTIONS = env.str(
        "{{ cookiecutter.project_slug | upper() }}_X_FRAME_OPTIONS",
        default="SAMEORIGIN",
    )
    SECURE_HSTS_SECONDS = env.int(
        "{{ cookiecutter.project_slug | upper() }}_SECURE_HSTS_SECONDS",
        default=31536000,
    )  # 1 year
    SESSION_COOKIE_NAME = "s"
    CSRF_COOKIE_NAME = "c"

    SITE_ID = env.int("SITE_ID", default=1)

    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    APPEND_SLASH = True

    ANNON_RATE = env.int(
        "{{ cookiecutter.project_slug | upper() }}_ANNON_THROTTLE_RATE_PER_MIUTE",
        default=50,
    )
    USER_RATE = env.int(
        "{{ cookiecutter.project_slug | upper() }}_USER_THROTTLE_RATE_PER_MIUTE",
        default=100,
    )

    # REST FRAMEWORK SETTINGS
    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "{{ cookiecutter.project_slug }}.apps.accounts.custom_auth.BearerAuthentication",
        ),
        "DEFAULT_FILTER_BACKENDS": (
            "django_filters.rest_framework.DjangoFilterBackend",
        ),
        "DEFAULT_PERMISSION_CLASSES": (
            "rest_framework.permissions.IsAuthenticated",
        ),
        "DEFAULT_PAGINATION_CLASS": (
            "{{ cookiecutter.project_slug }}.apps.common.pagination.DynamicPageSizePagination"
        ),
        "PAGE_SIZE": 20,
        "DEFAULT_THROTTLE_CLASSES": [
            "rest_framework.throttling.AnonRateThrottle",
            "rest_framework.throttling.UserRateThrottle",
        ],
        "DEFAULT_THROTTLE_RATES": {
            # Set throttling rates here
            "anon": f"{ANNON_RATE}/minute",
            "user": f"{USER_RATE}/minute",
        },
        "TEST_REQUEST_DEFAULT_FORMAT": "json",
    }

    # Rest and all auth configurations
    REST_AUTH_SERIALIZERS = {
        # Add custom serializers for Rest Auth
        "LOGIN_SERIALIZER": (
            "{{ cookiecutter.project_slug }}.apps.accounts.serializers.CustomLoginSerializer"
        ),
        "TOKEN_SERIALIZER": (
            "{{ cookiecutter.project_slug }}.apps.accounts.serializers.CustomTokenSerializer"
        ),
        "PASSWORD_RESET_SERIALIZER": (
            "{{ cookiecutter.project_slug }}.apps.accounts.serializers"
            + ".CustomPasswordResetSerializer"
        ),
        "PASSWORD_RESET_CONFIRM_SERIALIZER": (
            "{{ cookiecutter.project_slug }}.apps.accounts.serializers"
            + ".CustomPasswordResetConfirmSerializer"
        ),
    }

    REST_AUTH_REGISTER_SERIALIZERS = {
        "REGISTER_SERIALIZER": "{{ cookiecutter.project_slug }}.apps.accounts.serializers.CustomRegisterSerializer"
    }

    # Frontend URL to be used for password reset email, needs to be
    # of the form: <url>/<uid>/<token>, we will add the uid and token
    PASSWORD_RESET_URL = env.str(
        "{{ cookiecutter.project_slug | upper() }}_PASSWORD_RESET_URL",
        "http://localhost:3000/",
    )

    # Mandate the need for an Email Address when registering.
    ACCOUNT_EMAIL_REQUIRED = True

    # Choose whether to use Email or Username to login.
    # Omit to set as 'username'
    ACCOUNT_AUTHENTICATION_METHOD = "email"

    # Choose if user is logged out after changing password
    LOGOUT_ON_PASSWORD_CHANGE = env.bool(
        "{{ cookiecutter.project_slug | upper() }}_LOGOUT_ON_PASSWORD_CHANGE",
        default=True,
    )

    # Choose the username field. None if not using username.
    # Omit setting if using the default 'username' field.
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None

    # Choose whether a username is required during registration.
    # Omit setting if using the default 'username' field.
    ACCOUNT_USERNAME_REQUIRED = False

    # Choose whether old password needs to be entered when changing password
    OLD_PASSWORD_FIELD_ENABLED = env.bool(
        "{{ cookiecutter.project_slug | upper() }}_OLD_PASSWORD_ENABLED",
        default=True,
    )

    # Choose whether email verification is required before login is allowed.
    # Other options are: 'optional' , 'mandatory'
    ACCOUNT_EMAIL_VERIFICATION = env.str(
        "{{ cookiecutter.project_slug | upper() }}_EMAIL_VERIFICATION",
        default="none",
    )

    # Celery configurations
    CELERY_ACCEPT_CONTENT = ["json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_RESULT_BACKEND = "django-db"

    CELERY_CACHE_BACKEND = "default"

    # Swagger settings
    SWAGGER_SETTINGS = {
        "SECURITY_DEFINITIONS": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
            }
        }
    }

    # Custom configs and settings
    # Max page size for pagination, required since we are using dynamic page
    # size pagination
    MAX_PAGE_SIZE = env.int("MAX_PAGE_SIZE", 30)

    # Url prefixes and settings
    API_PREFIX = env.str(
        "{{ cookiecutter.project_slug | upper() }}_API_PREFIX", "api"
    )
    API_VERSION = env.str(
        "{{ cookiecutter.project_slug | upper() }}_API_VERSION", "v1"
    )
    PLATFORM_PREFIX = env.str(
        "{{ cookiecutter.project_slug | upper() }}_PLATFORM_PREFIX",
        "_platform",
    )
    DOCS_PREFIX = env.str(
        "{{ cookiecutter.project_slug | upper() }}_DOCS_PREFIX", "docs"
    )

    # Other settings
    COMMUNICATOR_NAME = env.str(
        "{{ cookiecutter.project_slug | upper() }}_MAIL_COMMUNICATOR_NAME",
        "Admin",
    )

    # For the docs
    CONTACT_EMAIL = env.str(
        "{{ cookiecutter.project_slug | upper() }}_CONTACT_EMAIL",
        "test@test.com",
    )
    SAMPLE_AUTH_TOKEN = env.str(
        "{{ cookiecutter.project_slug | upper() }}_SAMPLE_AUTH_TOKEN",
        "sjdhskjh3454343",
    )
    HOSTED_DOMAIN = env.str(
        "{{ cookiecutter.project_slug | upper() }}_HOSTED_DOMAIN",
        "https://ohuru.tech/",
    )
    API_DESCRIPTION_PATH = rel("docs", "README.md")
