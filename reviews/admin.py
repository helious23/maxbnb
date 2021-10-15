from django.contrib import admin
from . import models


@admin.register(models.Reivew)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    pass
