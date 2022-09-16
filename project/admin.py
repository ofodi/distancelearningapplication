from django.contrib import admin

from project.models import Authors, Courses

# Register your models here.
admin.site.register(Courses)

admin.site.register(Authors)