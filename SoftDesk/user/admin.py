from django.contrib.auth.admin import UserAdmin
from user.models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from user.models import CustomUser


class CustomAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    )


admin.site.register(CustomUser, CustomAdmin)

