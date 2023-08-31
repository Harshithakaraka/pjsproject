from django.contrib import admin

from .models import Mentor,Team,Department,Project

admin.site.register(Mentor)
admin.site.register(Team)
admin.site.register(Department)
admin.site.register(Project)