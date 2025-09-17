from django.contrib import admin
from .models import PromoCarousel, PromoSelfIntroduces, PromoSelfBeforeAfter

@admin.register(PromoCarousel)
class PromoCarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    # prepopulated_fields = {'slug': ('title',)}
    # readonly_fields = ['slug']  # Делаем поле только для чтения

@admin.register(PromoSelfIntroduces)
class PromoSelfIntroducesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

@admin.register(PromoSelfBeforeAfter)
class PromoSelfIntroducesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']