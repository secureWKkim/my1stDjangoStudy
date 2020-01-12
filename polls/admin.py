from django.contrib import admin
from .models import Question, Choice    # 아 같은 폴더에 있는건 이렇게 불러오는거구나...


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']  # 필터 기능
    search_fields = ['question_text']   # 검색 기능


admin.site.register(Question, QuestionAdmin)
