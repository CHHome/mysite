from django.contrib import admin

from .models import UserInfo
from  .models import user

admin.site.register(UserInfo)
admin.site.register(user)