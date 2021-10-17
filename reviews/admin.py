from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    # model 에서 작성한 __str__ method 를 사용하기 위해서 "__str__" 추가
    list_display = ("__str__", "rating_average")

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "user",
                    "room",
                    "review",
                )
            },
        ),
        (
            "Score",
            {
                "fields": (
                    "acurrancy",
                    "communication",
                    "cleanliness",
                    "location",
                    "check_in",
                    "value",
                )
            },
        ),
    )
    raw_id_fields = ("user", "room")
