from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [path("", room_views.all_rooms, name="home")]
# room_views.함수명은 /rooms/views.py 의 함수명과 일치해야됨
