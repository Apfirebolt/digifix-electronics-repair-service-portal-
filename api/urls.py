from django.urls import path
from django.conf.urls.static import static
from digifix_computer_repair import settings
from . views import ( UserAddressApiView, UserTestimonialApiView, CreateCustomUserApiView, ListCustomUsersApiView,
                      ComplaintListApiView, UserAddressCreateApiView, UserTestimonialCreateApiView,
                      UserTestimonialUpdateApiView, UserTestimonialDestroyApiView )
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup', CreateCustomUserApiView.as_view(), name='signup'),
    path('signin', obtain_auth_token, name='signin'),
    path('users', ListCustomUsersApiView.as_view(), name='users'),
    path('complaints', ComplaintListApiView.as_view(), name='complaints'),
    path('address', UserAddressApiView.as_view(), name='address'),
    path('address/add', UserAddressCreateApiView.as_view(), name='add-address'),
    path('testimonials', UserTestimonialApiView.as_view(), name='testimonial'),
    path('testimonials/add', UserTestimonialCreateApiView.as_view(), name='add-testimonial'),
    path('testimonials/<int:pk>/update', UserTestimonialUpdateApiView.as_view(), name='update-testimonial'),
    path('testimonials/<int:pk>/delete', UserTestimonialDestroyApiView.as_view(), name='delete-testimonial'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
