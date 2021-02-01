from django.contrib import admin
from courses.models import Course ,Prerequisite,Tag,Learning

admin.site.register(Course)
admin.site.register(Prerequisite)
admin.site.register(Tag)
admin.site.register(Learning)
