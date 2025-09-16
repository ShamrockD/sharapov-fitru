from django.shortcuts import render
from promo.models import PromoCarousel, PromoSelfIntroduces
from courses.models import CourseTag, Course, CourseCategory

def open_home_page(request):
    list_of_promotions = PromoCarousel.objects.all()
    list_of_self_introduces_images = PromoSelfIntroduces.objects.all()
    list_of_courses = Course.objects.all()
    list_of_course_categories = CourseCategory.objects.prefetch_related('course_set').all()
    context = {"carousel_objects": list_of_promotions,
               "self_introduces_images": list_of_self_introduces_images,
               "list_of_course_categories": list_of_course_categories,
               "list_of_courses": list_of_courses}
    return render(request=request, template_name="core/home.html", context=context)