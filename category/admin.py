from django.contrib import admin

from category.models import Category, ChatHistory


@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ['prompt', 'response', 'image', 'created_at']
    list_filter = ['prompt', 'response', 'created_at']
    ordering = ['prompt', 'response', 'created_at']
    search_fields = ['prompt', 'response', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'messages', 'table', 'created_at', 'modified_at']
    list_filter = ['name', 'user', 'created_at', 'modified_at']
    ordering = ['name', 'user', 'created_at', 'modified_at']
    search_fields = ['name', 'user', 'created_at', 'modified_at']
    readonly_fields = ['created_at', 'modified_at']
