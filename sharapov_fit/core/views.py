from django.shortcuts import render
from promo.models import PromoCarousel

def open_home_page(request):
    list_of_promotions = PromoCarousel.objects.all()
    context = {"carousel_objects": list_of_promotions}
    return render(request=request, template_name="core/home.html", context=context)