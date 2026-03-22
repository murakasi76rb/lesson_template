from django.contrib import admin

# Register your models here.
from apps.myapp.models import MenuItem, Cousine

admin.site.register(MenuItem)
admin.site.register(Cousine)
