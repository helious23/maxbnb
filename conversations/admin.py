from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Definition"""

    list_display = ("__str__", "created")
    fieldsets = (("Message", {"fields": ("message", "user", "conversation")}),)
    raw_id_fields = ("user", "conversation")


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """Conversation Admin Definition"""

    list_display = ("__str__", "count_messages", "count_participants")
    fieldsets = (("Conversation", {"fields": ("participants",)}),)
    filter_horizontal = ("participants",)
