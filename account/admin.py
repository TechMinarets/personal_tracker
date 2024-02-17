from django.contrib import admin

from account.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email'] 
    readonly_fields = ['uuid'] 
    list_filter = ['name'] 
    ordering = ['name']
