from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from perfiles.models import Usuario

# Register your models here.

admin.site.register(Usuario, UserAdmin)