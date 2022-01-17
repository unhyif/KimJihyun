from django.conf import settings
from django.db import models # Django의 Model
from django.utils import timezone


class Post(models.Model): # Model 정의
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # 글자 수가 제한된 텍스트 정의 =  짧은 문자열 정보 저장
    text = models.TextField() # 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(
            default=timezone.now) # 날짜, 시간
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title