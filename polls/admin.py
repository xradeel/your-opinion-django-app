from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                ["question"]
            ),
        }),
        ("Date Information", {
            "fields": (
                ["pub_date"]
            ),
            "classes": ['collapse']
        }),
    )
    inlines = [ChoiceInline]
    list_display = ["question", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question"]


admin.site.register(Question, QuestionAdmin)