from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """Time Stamped Modeol"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True

    # DB에 저장되는 model 이 아니므로 Meta class 생성하여 abstract = True 추가
    # 상속으로만 사용되는 class 임을 명시
