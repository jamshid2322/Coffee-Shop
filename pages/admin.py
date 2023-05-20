from django.contrib import admin
from pages.models import (
    Coffee,
    Feedback
)


@admin.register(Coffee)
class CoffeeAboutBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_about', 'is_blog')
    list_display_links = ("id", "title",)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'is_approved')
