from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import *

admin.site.register(MyUser)
admin.site.register(Session)
admin.site.register(Post)
