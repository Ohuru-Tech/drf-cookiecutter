import logging
import os

from django.core.management.base import BaseCommand
from drf_cookiecutter.apps.accounts.models import User

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

ADMIN_EMAIL = os.getenv(
    "DRF_COOKIECUTTER_ADMIN_EMAIL", "admin@drf_cookiecutter.com"
)
ADMIN_PASS = os.getenv("DRF_COOKIECUTTER_ADMIN_PASSWORD", "tempPassword@1234")


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            User.objects.create_superuser(
                email=ADMIN_EMAIL, password=ADMIN_PASS
            )
            logger.info(f"Admin User created with email: {ADMIN_EMAIL}")
        else:
            logger.info(
                "Admin user can only be created when "
                + "there are no existing users"
            )
