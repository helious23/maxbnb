from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True  # DB에 넣지 않음

    def __str__(self):
        return self.name  # class 이름 대신 name 을 리턴


# Room Type, Amenity 와 같은 항목은 하드 코딩 하는 대신
# django admin 기능을 이용하여 admin panel 에서 권한이 있는 user 가 직접
# 추가하거나 수정할 수 있게 함


class RoomType(AbstractItem):

    """Room Type Object Definition"""

    class Meta:
        verbose_name = "Room Type"  # Admin panel 에서 보여지는 Text 설정
        ordering = ["created"]  # 순서 설정 name: 알파벳 순

    pass


class Amenity(AbstractItem):

    """Amenity Type Object Definition"""

    class Meta:
        verbose_name_plural = "Amenities"  # 복수형 Text 설정

    pass


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"

    pass


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"

    pass


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    guests = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)  # ManyToOne

    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)  # ManyToMany
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rule = models.ManyToManyField("HouseRule", blank=True)

    # class 이름을 class.name 으로 다시 보여줌
    def __str__(self):
        return self.name
