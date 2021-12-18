from django.urls import path
from django.conf.urls.static import static
from digifix_computer_repair import settings
from . views import ( UserAddressApiView, UserTestimonialApiView )


urlpatterns = [
    path('address', UserAddressApiView.as_view(), name='address'),
    path('testimonials', UserTestimonialApiView.as_view(), name='testimonial'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
