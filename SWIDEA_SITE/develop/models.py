from django.db import models

class Tool(models.Model):
    name = models.CharField(">> 이름", max_length = 20)
    kind = models.CharField(">> 종류", max_length = 20)
    description = models.TextField(">> 개발툴 설명")
    
    def __str__(self):
        return self.name

class Idea(models.Model):
    title = models.CharField(">> 아이디어명", max_length = 20)
    image = models.ImageField(">> 대표 사진", blank=True)
    content = models.TextField(">> 아이디어 설명")
    interest = models.IntegerField(">> 아이디어 관심도")
    devtool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="ideas", verbose_name=">> 예상 개발툴")

    def __str__(self):
        return f"[{self.devtool.name}] {self.title}"





