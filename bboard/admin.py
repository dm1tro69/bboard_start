from django.contrib import admin
from .models import Bb, Rubric

# Register your models here.

@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric',)
    list_display_links = ('title', 'content', 'rubric',)
    search_fields = ('title', 'content', 'rubric',)


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
