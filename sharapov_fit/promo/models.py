from django.db import models

class PromoCarousel(models.Model):
    title = models.CharField(verbose_name="Название", 
                             max_length=255,
                             unique=True)
    slug = models.SlugField(verbose_name="SLUG", 
                            max_length=255,
                            unique=True)
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