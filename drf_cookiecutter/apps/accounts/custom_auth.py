from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Bearer ".  For example:

        Authorization: Bearer 401f7ac837da42b97f613d789819ff93537bee6a

    """

    keyword = "Bearer"
