from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Post)

# Register your models here.
