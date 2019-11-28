from django.db import models
from django.utils import timezone


class Interaction(models.Model):
    """
    Represent a specific interaction with the application.

    Interactions are used to log specific events, e.g.
    the creation of an object.
    """
    timestamp = models.DateTimeField(default=timezone.now)
    interaction_type = models.TextField()

    def __str__(self):
        return "<Interaction: {}>".format(self.interaction_type)
