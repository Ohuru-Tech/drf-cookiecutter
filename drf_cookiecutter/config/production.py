from .base import Common
from .environment import env


class Prod(Common):
    # Keep debug true in development
    DEBUG = False

    # Restrict the allowed hosts
    ALLOWED_HOSTS = env.list(
        "DRF_COOKIECUTTER_PROD_ALLOWED_HOSTS",
        default=[
            "127.0.0.1",
            "localhost",
        ],
    )

    # Use local database
    DATABASES = {
        "default": env.db(
            "DRF_COOKIECUTTER_DATABASE_URL_PROD",
            default="psql://postgres:@database:5432/drf_cookiecutter_db",
        )
    }

    # Mail
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_PORT = env.str("DRF_COOKIECUTTER_EMAIL_PORT", default="1025")
    EMAIL_HOST = env.str(
        "DRF_COOKIECUTTER_EMAIL_HOST",
        default="127.0.0.1",
    )
    EMAIL_HOST_USER = env.str(
        "DRF_COOKIECUTTER_EMAIL_HOST_USER",
        default="user",
    )
    EMAIL_HOST_PASSWORD = env.str(
        "DRF_COOKIECUTTER_EMAIL_HOST_PASSWORD",
        default="password",
    )
    EMAIL_USE_TLS = env.bool("DRF_COOKIECUTTER_EMAIL_USE_TLS", default=True)

    # Disable CORS check
    CORS_ALLOWED_ORIGINS = env.list(
        "DRF_COOKIECUTTER_CORS_WHITELIST",
        default=["http://localhost:8000", "http://127.0.0.1:8000"],
    )

    # Celery broker config
    BROKER_URL = env.str(
        "DRF_COOKIECUTTER_CELERY_BROKER_PROD",
        default="amqp://drf_cookiecutter:pass@localhost:5672/drf_cookiecutter",
    )
