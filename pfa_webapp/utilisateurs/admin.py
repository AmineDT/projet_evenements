from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile


# Register your models here.
class UserAdminConfig(UserAdmin):
    readonly_fields = ('date_joined', 'last_login',)
    ordering = ('-date_joined',)
    list_display = (
        'username', 'email', 'date_joined', 'club_joined'

    )
    list_filter = ('is_active', 'is_superuser', 'club_joined')

    fieldsets = (
        (None, {
            # 'classes': ('collapse',),
            'fields': ('email', 'password')
        }),
        ('Personal Info', {
            'fields': (('first_name', 'last_name'),
                       )
        }),
        ('Additional Info', {
            'fields': (('club_joined'),
                       )
        }),
        ('Fundamental Permissions', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
        ('Group Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions',)
        }),

    )


admin.site.register(UserProfile, UserAdminConfig)
