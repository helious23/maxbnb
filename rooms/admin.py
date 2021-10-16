from django.contrib import admin
from . import models


@admin.register(
    models.RoomType, models.Facility, models.Amenity, models.HouseRule
)  # 여러 class 를 admin 에 한번에 등록 가능: 등록해야 추가 및 수정 가능
class ItemAdmin(admin.ModelAdmin):
    # RoomType, Facility, Amenity, HouseRule 모두 AbstractItem 을 상속하므로
    # ItemAdmin 이라는 class 를 만들어서 admin 에 register

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse",),  # 접을 수 있는 fieldset
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rule",
                ),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    # 순서대로 정렬 가능하게 함
    # ordering = ("name", "price", "guests")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "country",
    )

    # admin search 에 검색할 fields 지정
    # room model 의 host 에서 user 접근하기 위해서 host__username
    # "=keyword" : iexact - 정확하게 일치
    # "^keyword" : startswith - 앞부분 일치
    # "keyword" : icontains - 대소문자 구분 X
    search_fields = ("^city", "^host__username")

    # ManytoMany field 에만 적용
    # 왼쪽 오른쪽으로 나눠 선택할 수 있게 함
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )

    # list_fields 에 적용할 method
    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "# Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "# Photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass
