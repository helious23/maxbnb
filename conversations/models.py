from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField(
        "users.user", related_name="conversation", blank=True
    )

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    """Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages", on_delete=CASCADE)
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
