from django.contrib import admin
from .models import UserInfo
from .models import Pairing

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Pairing)

