from autoslug import AutoSlugField
from django.db import models

class CourseTag(models.Model):
    title = models.CharField(verbose_name="Название", 
                             max_length=255, 
                             unique=True)
    slug = AutoSlugField(verbose_name="SLUG", 
                         populate_from='title',
                         unique=True,
                         always_update=True)
    short_description = models.TextField(verbose_name="Краткое описание", 
                                         max_length=1000, 
                                         blank=True, 
                                         null=True)
    full_description = models.TextField(verbose_name="Полное описание",
                                        max_length=10000, 
                                        blank=True, 
                                        null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Тэг курса"
        verbose_name_plural = "Тэги курсов"

class CourseCategory(models.Model):
    title = models.CharField(verbose_name="Название", 
                             max_length=255, 
                             unique=True)
    slug = AutoSlugField(verbose_name="SLUG", 
                         populate_from='title',
                         unique=True,
                         always_update=True)
    short_description = models.TextField(verbose_name="Краткое описание", 
                                         max_length=1000, 
                                         blank=True, 
                                         null=True)
    full_description = models.TextField(verbose_name="Полное описание",
                                        max_length=10000, 
                                        blank=True, 
                                        null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория курса"
        verbose_name_plural = "Категории курсов"
        
class Course(models.Model):
    title = models.CharField(verbose_name="Название", 
                             max_length=255, 
                             unique=True)
    slug = AutoSlugField(verbose_name="SLUG", 
                         populate_from='title',
                         unique=True,
                         always_update=True)
    course_logo = models.ImageField(verbose_name="Изображение", 
                              upload_to="courses/courses_logo/",
                              blank=True,
                              null=True)
    short_description = models.TextField(verbose_name="Краткое описание", 
                                         max_length=1000, 
                                         blank=True, 
                                         null=True)
    full_description = models.TextField(verbose_name="Полное описание",
                                        max_length=10000, 
                                        blank=True, 
                                        null=True)
    categories = models.ManyToManyField(to=CourseCategory, 
                                        verbose_name="Категории", 
                                        null=True, 
                                        blank=True)
    tags = models.ManyToManyField(to=CourseTag, 
                                        verbose_name="Тэги", 
                                        blank=True, 
                                        null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"