from django.contrib import admin
from .models import Segouser

# Register your models here.


class SegouserAdmin(admin.ModelAdmin):
	list_display = ['username','email','password']

admin.site.register(Segouser, SegouserAdmin)