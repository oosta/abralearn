from django.contrib import admin
from .models import User, Course, Progress

# Register your models here
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Progress)
