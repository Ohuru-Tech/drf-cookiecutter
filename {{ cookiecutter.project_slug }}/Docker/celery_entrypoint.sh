#!/bin/bash

set -e

function help_text() {
  cat << 'END'                                               
Docker entrypoint script for Celery. Unless specified, all commands
will wait for the database to be ready.
Usage:
  help - print this help text and exit
  start - start the celery worker
  (anything else) - run the command provided
END
}


function header() {
  size=${COLUMNS:-80}
  # Print centered text between two dividers of length $size
  printf '#%.0s' $(seq 1 $size) && echo
  printf "%*s\n" $(( (${#1} + size) / 2)) "$1"
  printf '#%.0s' $(seq 1 $size) && echo
}

if [ "$1" == help ] || [ "$1" == --help ]; then help_text && exit 0; fi
sleep 0.1;  # The $COLUMNS variable takes a moment to populate

# Wait for database
header "WAITING FOR DATABASE"
python Docker/wait_for_db.py

case "$1" in
  start|"")
    # Start celery worker
    header "Starting celery worker"
    celery -A {{ cookiecutter.project_slug }} worker -l info
    ;;
  *)
    # The command is something like bash. Just run it in the right environment.
    header "RUNNING \"$*\""
    exec "$@"
    ;;
esac
