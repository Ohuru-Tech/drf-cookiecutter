from .base import Common
from .environment import env


class Prod(Common):
    # Keep debug true in development
    DEBUG = False

    # Restrict the allowed hosts
    ALLOWED_HOSTS = env.list(
        "{{ cookiecutter.project_slug | upper() }}_PROD_ALLOWED_HOSTS",
        default=[
            "127.0.0.1",
            "localhost",
        ],
    )

    # Use local database
    DATABASES = {
        "default": env.db(
            "{{ cookiecutter.project_slug | upper() }}_DATABASE_URL_PROD",
            default="{{ cookiecutter.prod_db_url }}",
        )
    }

    # Mail
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_PORT = env.str(
        "{{ cookiecutter.project_slug | upper() }}_EMAIL_PORT", default="1025"
    )
    EMAIL_HOST = env.str(
        "{{ cookiecutter.project_slug | upper() }}_EMAIL_HOST",
        default="127.0.0.1",
    )
    EMAIL_HOST_USER = env.str(
        "{{ cookiecutter.project_slug | upper() }}_EMAIL_HOST_USER",
        default="user",
    )
    EMAIL_HOST_PASSWORD = env.str(
        "{{ cookiecutter.project_slug | upper() }}_EMAIL_HOST_PASSWORD",
        default="password",
    )
    EMAIL_USE_TLS = env.bool(
        "{{ cookiecutter.project_slug | upper() }}_EMAIL_USE_TLS", default=True
    )

    # Disable CORS check
    CORS_ALLOWED_ORIGINS = env.list(
        "{{ cookiecutter.project_slug | upper() }}_CORS_WHITELIST",
        default=["http://localhost:8000", "http://127.0.0.1:8000"],
    )

    # Celery broker config
    BROKER_URL = env.str(
        "{{ cookiecutter.project_slug | upper() }}_CELERY_BROKER_PROD",
        default="amqp://{{ cookiecutter.project_slug }}:pass@localhost:5672/{{ cookiecutter.project_slug }}",
    )
