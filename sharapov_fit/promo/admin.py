from django.contrib import admin
from .models import PromoCarousel

@admin.register(PromoCarousel)
class PromoCarouselAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}