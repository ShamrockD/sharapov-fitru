from django.shortcuts import render
from promo.models import PromoCarousel, PromoSelfIntroduces

def open_home_page(request):
    list_of_promotions = PromoCarousel.objects.all()
    list_of_self_introduces_images = PromoSelfIntroduces.objects.all()
    context = {"carousel_objects": list_of_promotions,
               "self_introduces_images": list_of_self_introduces_images}
    return render(request=request, template_name="core/home.html", context=context)