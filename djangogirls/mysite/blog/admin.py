from django.contrib import admin
from .models import Post # Post 모델

admin.site.register(Post) # 만든 모델을 관리자 페이지에서 보기 위해 모델 등록