from django.contrib import admin
from .models import Question, Choice


admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin'
admin.site.index_title = 'Pollster Administration'


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'question_text'
            ],
        }),
        ('Date Information', {
            'fields': [
                'pub_date'
            ],
            'classes': [
                'collapse'
            ],
        }),
    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
