from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # auto_now_add : 생성시에 자동 저장
    updated = models.DateTimeField(auto_now=True)  # auto_now : update 시에 자동 저장
    objects = managers.CustomModelManager()  # 모든 models 에 objects.get_or_none(...) 사용할 수 있게 함

    class Meta:
        abstract = True

    # DB에 저장되는 model 이 아니므로 Meta class 생성하여 abstract = True 추가
    # 상속으로만 사용되는 class 임을 명시
