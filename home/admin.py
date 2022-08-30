from django.contrib import admin
from home.models import General_info, Project, Jobs, Experience


# Register your models here.
admin.site.register(General_info)
admin.site.register(Project)
admin.site.register(Jobs)
admin.site.register(Experience)