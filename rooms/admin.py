from django.contrib import admin
from . import models


@admin.register(
    models.RoomType, models.Facility, models.Amenity, models.HouseRule
)  # 여러 class 를 admin 에 한번에 등록 가능: 등록해야 추가 및 수정 가능
class ItemAdmin(admin.ModelAdmin):
    # RoomType, Facility, Amenity, HouseRule 모두 AbstractItem 을 상속하므로
    # ItemAdmin 이라는 class 를 만들어서 admin 에 register

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass
