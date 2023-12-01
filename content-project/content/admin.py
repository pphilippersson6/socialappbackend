from django.contrib import admin
from .models import *

# Register the admin classes with the admin site
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Follow)
