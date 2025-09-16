from django.contrib import admin
from .models import CourseCategory, Course, CourseTag

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    pass