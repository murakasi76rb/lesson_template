from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from apps.myapp.models import MenuItem

admin.site.register(MenuItem)

=======
from apps.myapp.models import MenuItem, Cousine

admin.site.register(MenuItem)
admin.site.register(Cousine)
>>>>>>> refs/remotes/origin/feature1
