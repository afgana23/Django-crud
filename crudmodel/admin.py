from django.contrib import admin
from .models import MyUser
@admin.register(MyUser)
# Register your models here.
class myuseradmin(admin.ModelAdmin):
    list_display=("id",'username','password')