from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "page"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):  # context 수정할 수 있는 함수
        context = super().get_context_data(
            **kwargs
        )  # super() 로 기존의 context 를 유지시켜 줘야 됨
        return context
