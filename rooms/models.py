from django.db import models
from django.urls import reverse
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
# django admin 기능을 이용하여 admin panel 에서
# 권한이 있는 user 가 직접 추가하거나 수정할 수 있게 함


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


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    price = models.IntegerField()

    guests = models.IntegerField(help_text="How many people will be staying?")
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()

    check_in = models.TimeField()
    check_out = models.TimeField()

    instant_book = models.BooleanField(default=False)

    # room 에서 user(host)를 찾을 때 사용하는 method 변경 시,
    # related_name 사용하여 변경
    # default: room_set -> rooms
    # user.room.all()
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )  # ManyToOne

    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    # ManyToMany
    # ManyToMany 관계에서도 반대의 관계에서 query 를 호출할 경우가 있으므로
    # related_name 설정 : amenities.room_set.all() -> amenities.roooms.all()
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rule = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    # class 이름을 class.name 으로 다시 보여줌
    def __str__(self):
        return self.name

    # model 자체를 intercept 하여 부모 class (models.Model) 의 save() method override
    # model 을 intercept 하는것이므로 admin panel 에서의 수정 뿐만 아니라
    # 다른 모든 수정 상황에서 적용됨 ex) frontend, admin 등
    def save(self, *args, **kwargs):
        self.city = self.city.title()
        super().save(*args, **kwargs)

    # admin panel 에서 view on site 의 경로 지정
    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
        # reverse("config.urls.namespace:rooms:urls.name")

    def total_acurrancy(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.acurrancy
        try:
            return round(all_ratings / len(all_reviews), 1)
        except ZeroDivisionError:
            return 0

    def total_communication(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.communication
        try:
            return round(all_ratings / len(all_reviews), 1)
        except ZeroDivisionError:
            return 0

    def total_cleanliness(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.cleanliness
        try:
            return round(all_ratings / len(all_reviews), 1)
        except ZeroDivisionError:
            return 0

    def total_location(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.location
        try:
            return round(all_ratings / len(all_reviews), 1)
        except ZeroDivisionError:
            return 0

    def total_check_in(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.check_in
        try:
            return round(all_ratings / len(all_reviews), 1)
        except ZeroDivisionError:
            return 0

    def total_value(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.value
        try:
            return round(all_ratings / len(all_reviews), 1)
        except ZeroDivisionError:
            return 0

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        try:
            return round(all_ratings / len(all_reviews), 2)
        except ZeroDivisionError:
            return 0

    def first_photo(self):
        (photo,) = self.photos.all()[:1]
        return photo.file.url

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    # uploads 폴더 내에 user_id/room_photos_room_id/파일명 으로 저장
    def user_directory_path(instance, filename):
        return "user_{0}/room_photos/room_{1}/{2}".format(
            instance.room.host.id, instance.room.id, filename
        )

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to=user_directory_path)
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
