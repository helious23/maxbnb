from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    print(vars(rooms.paginator))
    return render(
        request, "rooms/home.html", context={"rooms": rooms}
    )  # html 파일 명은 /templates 안의 html 파일명과 일치해야됨
    # context - html 로 넘기는 변수
