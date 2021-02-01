from django.contrib import admin
from courses.models import Course ,Prerequisite,Tag,Learning

class TagAdmin(admin.TabularInline):
        model = Tag

class PrerequisiteAdmin(admin.TabularInline):
        model = Prerequisite

class LearningAdmin(admin.TabularInline):
    model = Learning

class CourseAdmin(admin.ModelAdmin):
    inlines = [ TagAdmin, PrerequisiteAdmin, LearningAdmin]

admin.site.register(Course,CourseAdmin)

