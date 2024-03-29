FROM python:3.9-slim

# Create a group and user to run our app
ENV APP_USER={{ cookiecutter.project_slug }}_user
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

# Install packages needed to run your application (not build deps):
#   mime-support -- for mime types when serving static files
#   postgresql-client -- for running database commands
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN set -ex \
    && RUN_DEPS=" \
    libpcre3 \
    mime-support \
    postgresql-client \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Determine if we are going to use the dev or prod stuff
ENV RUNTIME=Prod
# Copy in your pord requirements file
ADD requirements_${RUNTIME}.txt /requirements.txt

# Install build deps, then run `pip install`, then remove unneeded build deps
# all in a single step.
# Correct the path to your production requirements file, if needed.
RUN set -ex \
    && BUILD_DEPS=" \
    build-essential \
    libpcre3-dev \
    libpq-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip install --no-cache-dir -r /requirements.txt \
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Copy your application code to the container (make sure you create a .dockerignore 
# file if any large files or directories should be excluded)
RUN mkdir /{{ cookiecutter.project_slug }}/
WORKDIR /{{ cookiecutter.project_slug }}/
ADD . /{{ cookiecutter.project_slug }}/
RUN chown ${APP_USER}:${APP_USER} /{{ cookiecutter.project_slug }}/

# uWSGI will listen on this port
EXPOSE 8000

# Set up required env variables for managepy to run
ENV DJANGO_SETTINGS_MODULE="{{ cookiecutter.project_slug }}.config"
ENV DJANGO_CONFIGURATION=${RUNTIME}
ENV {{ cookiecutter.project_slug | upper() }}_DATABASE_URL_DEV={{ cookiecutter.dev_db_url }}
ENV {{ cookiecutter.project_slug | upper() }}_DATABASE_URL_PROD={{ cookiecutter.prod_db_url }}

# Call collectstatic:
RUN python manage.py collectstatic --noinput

# Tell uWSGI where to find your wsgi file :
ENV UWSGI_WSGI_FILE={{ cookiecutter.project_slug }}/wsgi.py

# Base uWSGI configuration (you shouldn't need to change these):
ENV UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Number of uWSGI workers and threads per worker (customize as needed):
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

# uWSGI static file serving configuration (customize or comment out if not needed):
ENV UWSGI_STATIC_MAP="/static/=/{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}/static_collected/" UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"

# Deny invalid hosts before they get to Django (uncomment and change to your hostname(s)):
# ENV UWSGI_ROUTE_HOST="^(?!localhost:8000$) break:400"

# Change to a non-root user
USER ${APP_USER}:${APP_USER}
# Comment or uncomment if it is available
ENTRYPOINT ["bash", "/{{ cookiecutter.project_slug }}/Docker/entrypoint.sh"]

# Start uWSGI when entrypoint is there
# Change it to any other command based on your file
# Do not use the init command for dev, the app user does not have  required permissions
CMD ["server"]
