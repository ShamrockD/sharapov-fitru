from autoslug import AutoSlugField
from django.db import models

class PromoCarousel(models.Model):
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
    is_active_promo = models.BooleanField(verbose_name="Активное промо?", 
                                          default=False)
    image = models.ImageField(verbose_name="Изображение", 
                              upload_to="promo/promocarousel/",
                              blank=True,
                              null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Промо карусель"
        verbose_name_plural = "Промо карусели"
        
class PromoSelfIntroduces(models.Model):
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
    is_active_promo = models.BooleanField(verbose_name="Активное промо?", 
                                          default=False)
    image = models.ImageField(verbose_name="Изображение", 
                              upload_to="promo/selfintroduces/",
                              blank=True,
                              null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Промо личный пример"
        verbose_name_plural = "Промо личные примеры"
        
class PromoSelfBeforeAfter(models.Model):
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
    full_description = models.TextField(verbose_name="Краткое описание", 
                                         max_length=1000, 
                                         blank=True, 
                                         null=True)
    is_active = models.BooleanField(verbose_name="Активный?", 
                                    default=False)
    video = models.FileField(verbose_name="Видео файл", 
                             upload_to="promo/videos/selfbeforeafter",
                             blank=True, 
                             null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Видео до и после"
        verbose_name_plural = "Видео до и после"