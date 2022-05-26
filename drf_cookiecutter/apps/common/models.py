from django.db import models


class BlackList(models.Model):
    """
    Will contain all the emails that do not exist but somehow end up in some
    of the forms.
    """

    email = models.EmailField()

    def __str__(self):
        return self.email
