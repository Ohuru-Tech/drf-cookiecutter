# {{ cookiecutter.project_name }}
This project is the starting point for a new django backend project. It is based on the DRF framework.

# Project dev details

## App Structure
All the apps are located in the `{{ cookiecutter.project_slug }}/apps` folder. The project uses a custom `startapp` command, refer `{{ cookiecutter.project_slug }}/management/commands/startapp.py` for more information.

The command initializes a new app with the following:
- A models directory as opposed to a generic `models.py` file which is created by Django's default `startapp` command, this allows you to have models separated by their use-case and helps to keep the project clean.
- A `views` directory which corresponds to the above reasoning for having a models directory.
- A `seriazliers` directory which corresponds to the above reasoning for having a models directory.

The other files and folders are similar to how Django does (`admin.py`, `apps.py`).

This command ensures that the apps are added to the `apps` folder and are initialized in accordance with the project-setup.
To add a new app run:
```bash
$ python manage.py startapp <app_name>
```
Then include the app to the `INSTALLED_APPS` list in `config/base.py` like so:
```python
INSTALLED_APPS = [
    ...
    '{{ cookiecutter.project_slug }}.apps.<app_name>.apps.<app_name_capitalized>Config',
    ...
]
```
eg: if your `app_name` is `foo` then this would be:
```python
INSTALLED_APPS = [
    ...
    '{{ cookiecutter.project_slug }}.apps.foo.apps.FooConfig',
    ...
]
```

It is always nice to include the complete config while adding the app in the `INSTALLED_APPS` list. This maintains consistency when using signals.

## Settings

The project uses [`django-configurations`](https://django-configurations.readthedocs.io/en/stable/) for class based settings, there are two configurations available, `Dev` and `Prod`, the common settings exist in `config/base.py`, `Dev` in `config/dev.py` and  `Prod` in `config/prod.py`.

You can use the `DJANGO_CONFIGURATION` environment variable to switch between the configurations, the `Dev` settings are used by default.

### Environment Variables
Most of the configurations in the project are based on environment variables, you have the following options to use them:
- Set them up in a `.env` file in the root of the project, i.e. the place where you have this `README.md` file, you can refer to the `.env.template` for the available options and easily create your configuration file using that.
- Set them up via the environment variables themselves.
- Set them up in the docker / kubernetes runtime via the `.env` file, most of the things still remain the same except that you will need to get rid of the comments in `.env.template` while creating the `.env` file.

You can still run the project without creating any of those files because there are defaults available to almost all of the required settings but, you will need to set up the db instances, rabbit mq (in case you want to use celery) and make sure the settings match the ones used by default in the configurations. It is recommended to always have a `.env` file managing these settings.

## Documentation
The project uses `drf-yasg` to auto-create documentation for the API endpoints, but the generated documentation is not very good, hence, this project uses a custom schema to manage the documentation.

The details for each endpoint are managed using a class, for example, the `accounts` app supports profile update, so the `ProfileUpdate` class is used to manage the documentation for that endpoint, it looks something like this:
    
```python
class ProfileUpdate:
    desc = f"""
Profile Update is an API endpoint to update the profile associated
with a particular user.

By using this endpoint, you can make a patch call to update the profile
associated with any user. The {fields_to_md(ProfileCreateUpdateSerializer.fields_names)}
are the fields that can currently be updated
    """  # noqa

    responses = {
        "200": openapi.Response(
            description="OK",
            examples=profile_update_200_example,
            schema=UserInfoSerializer,
        ),
        "401": openapi.Response(
            description="Unauthorized", examples=profile_update_401_example
        ),
        "403": openapi.Response(
            description="Permission Denied",
            examples=profile_update_403_example,
        ),
    }

    code_examples = [{"lang": "Bash", "source": profile_update_curl}]

    swagger_setup = {
        "operation_id": "Profile Update",
        "operation_description": desc,
        "request_body": ProfileCreateUpdateSerializer,
        "responses": responses,
        "code_examples": code_examples,
    }
```

The examples come from `config/examples` and look something like this:
```python
profile_update_200_example = {
    "application/json": {
        "id": 1,
        "name": "Test developer",
        "profile_pic": "/some_pic.jpg"
    },
}

profile_update_401_example = {
    "application/json": {
        "error": "NotAuthenticated",
        "detail": "Incorrect authentication credentials.",  # noqa
    }
}

profile_update_403_example = {
    "application/json": {
        "error": "PermissionDenied",
        "detail": "You do not have permission to perform this action."
    }
}
```

After setting up the class, you can use the `swagger_auto_schema` decorator to plug the specification into the view.

```python
@method_decorator(
    swagger_auto_schema(**ProfileUpdate.swagger_setup), "partial_update"
)
class ProfileViewSet(UpdateModelMixin, PsqMixin, GenericViewSet):
    ...
```

In the above example, the `ProfileUpdate` class we declared earlier is used to plug those settings onto the `partial_update` action.

## The views

The project is set up to use [`GenericViewSet`](https://www.django-rest-framework.org/api-guide/viewsets/#genericviewset), it further uses different [`mixins`](https://www.django-rest-framework.org/api-guide/generic-views/#mixins) to provide the `create`, `retrieve`, `update` and `destroy` actions.
You can set up custom actions for anything else that you might need to do.

The views also use the [`PsqMixin`](https://github.com/drf-psq/drf-psq#1-psqmixin-class) to configure different serizlizers and permissions for the actions. The serializers come from the `serializers` directory and the permissions are from the `permissions` directory (or file, as per your convinience).

## Routers
The `GenericViewSet` automatically sets up the URLs based on the mixins you use with it, it also adds the custom actions as urls. Thus, we have `urls/versioned_urls.py` which uses a [`SimpleRouter`](https://www.django-rest-framework.org/api-guide/routers/#simplerouter) to add these viewsets and plug them at different endpoints.

### Versioning
The version comes from the environment variables, you can set it up in the `.env` file. To add and support different versions, you can have differnt `urls` list in the `urls/versioned_urls.py` file, then update the environment to default to the latest version. You can manually include the other versions in `urls/__init__.py` as and when needed.

## Database
The project supports PostgreSQL, PostGIS, MySQL, MySQL (GIS), Oracle, Oracle (GIS), Redshift, CockroachDB, and SQLite, you can refer [this](https://github.com/jazzband/dj-database-url#url-schema) table in order to find out the details on forming the url corresponding to your database.

# Project deployment
The project contains a production-ready `Dockerfile`, refer `Docker/Docerfile.web` and `Docker/Dockerfile.celery` for more details. You can use these dockerfiles with either `docker-compose` or `kubernetes` to deploy the project.

The Dockerfile uses `uwsgi` to run the project, this allows for serving `static` and `media` files right from your container.

The support for `kubernetes` is not yet implemented, but it is planned to be implemented soon.
