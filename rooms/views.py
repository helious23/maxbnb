from django.shortcuts import render
from . import models


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(
        request, "rooms/home.html", context={"rooms": all_rooms}
    )  # html 파일 명은 /templates 안의 html 파일명과 일치해야됨
    # context - html 로 넘기는 변수
