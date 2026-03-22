from django.contrib import admin

# Register your models here.

from apps.myapp.models import MenuItem

admin.site.register(MenuItem)

