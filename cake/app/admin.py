from django.contrib import admin
from .models import Cake,UserProfile
from django.contrib.auth.models import User

class MemberAdmin(admin.ModelAdmin):
 list_display=("name","email","mobilenumber","address","quantity","description",)

admin.site.register(Cake,MemberAdmin)
admin.site.register(UserProfile)
