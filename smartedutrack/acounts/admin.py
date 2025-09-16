from django.contrib import admin

# Register your models here.

from .models import User  # import your custom user model

admin.site.register(User)  # register the model so it appears in admin
