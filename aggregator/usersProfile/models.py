from django.db import models
from djangoPlatform.apps.aggregator.models import TimestampedModel


class Profile(TimestampedModel):
    # There is an inherent relationship between the Profile and
    # User models. By creating a one-to-one relationship between the two, we
    # are formalizing this relationship. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)
   # created_at = models.DateTimeField(auto_now_add=True)
   # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
