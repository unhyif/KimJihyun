from django.db import models
from datetime import *

class Review(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)

    YEAR_CHOICES = [(y,y) for y in range(1950, (datetime.now().year+1))]
    year = models.PositiveSmallIntegerField(verbose_name='개봉년도', choices=YEAR_CHOICES)
    director = models.CharField(verbose_name='감독', max_length=100)
    actor = models.CharField(verbose_name='주연', max_length=200)

    GENRE_CHOICES = [
        ('ACT', '액션'),
        ('COM', '코미디'),
        ('DR', '드라마'),
        ('RO', '로맨스'),
        ('HO', '공포'),
        ('TH', '스릴러'),
        ('SF', 'SF'),
        ('FAN', '판타지'),
        ('ANI', '애니메이션'),
        ('DOC', '다큐멘터리'),
        ('IN', '독립영화'),
        ('ETC', '기타')
    ]
    genre = models.CharField(verbose_name='장르', max_length=3, choices=GENRE_CHOICES)
    running_time = models.PositiveSmallIntegerField(verbose_name='러닝타임 (분)')

    RATING_CHOICES = [(0.5*i, 0.5*i) for i in range(1, 11)]
    rating = models.FloatField(verbose_name='별점', choices=RATING_CHOICES)
    review = models.TextField(verbose_name='리뷰')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def running_time_by_hour(self):
        h, m = "", ""
        if self.running_time//60:
            h = f"{self.running_time//60}시간 "
        if self.running_time%60:
            m = f"{self.running_time%60}분"
        return h+m