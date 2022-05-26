import logging
import os
import sqlite3
import sys
import time
from urllib.parse import urlparse

import psycopg2

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s:  %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

TRIES = 10
RUNTIME = os.getenv("DJANGO_CONFIGURATION")
CONN_ID = os.getenv(
    f"{{ cookiecutter.project_slug | upper() }}_DATABASE_URL_{RUNTIME.upper()}"
)
print(CONN_ID)


def main():
    db_available = _wait_for_db()
    if not db_available:
        logger.error(f"Could not connect to DB using conn_id {CONN_ID}")
        sys.exit(1)
    else:
        sys.exit(0)


def _wait_for_db(tries=TRIES, conn_id=CONN_ID):
    db_details = urlparse(conn_id)
    success = False
    for i in range(1, TRIES + 1):
        try:
            logger.info(f"Testing DB connection {conn_id}")
            if db_details.hostname:
                connection = psycopg2.connect(
                    host=db_details.hostname,
                    port=db_details.port,
                    dbname=db_details.path[1:],
                    user=db_details.username,
                    password=db_details.password,
                )
            else:
                connection = sqlite3.connect(db_details.path[1:])
            connection.close()
            success = True
            logger.info(f"Succesfully tested connection {conn_id}")
            break
        except (psycopg2.OperationalError, sqlite3.OperationalError) as oe:
            logger.info("DB not yet available")
            logger.debug(f"Error was:  {oe}")
            logger.info(f"Waiting {i} seconds...")
            # Back off with each loop to give the DB a chance to appear.
            time.sleep(i)
    return success


if __name__ == "__main__":
    main()
