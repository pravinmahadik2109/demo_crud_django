from django.contrib import admin
from .models import Superadmin, NormalUser

admin.site.register(Superadmin)
admin.site.register(NormalUser)
