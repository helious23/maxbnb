from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
# room_views.함수명은 /rooms/views.py 의 함수명과 일치해야됨
# class based view 사용 시, path("url", class경로.as_view(), name="xxx")
# class 를 functoin 으로 변환 : as_view() 사용
