from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 원칙적으로 임의의 메서드에 의한 값은 정렬 불가. 대신 다른 값 기준으로 정렬 가능. 여기서 이 기준 항목을 설정.
    was_published_recently.admin_order_field = 'pub_date'
    # True 설정하면 값 대신 아이콘이 나타난다(실제 화면)
    was_published_recently.boolean = True
    # 항목의 헤더 이름 설정.
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 종속,연속,직렬
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
