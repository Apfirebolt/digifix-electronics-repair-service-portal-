from django.urls import path
from django.conf.urls.static import static
from digifix_computer_repair import settings
from . views import ( UserAddressApiView, UserTestimonialApiView, CreateCustomUserApiView, ListCustomUsersApiView,
                      ComplaintListApiView, ComplaintCreateApiView, ComplaintUpdateApiView,
                      AddCommentApiView, UpdateCommentApiView, DestroyCommentApiView, ListCommentApiView,
                      UserAddressCreateApiView, UserAddressDestroyApiView, UserAddressUpdateApiView,
                      UserTestimonialCreateApiView, UserTestimonialUpdateApiView, UserTestimonialDestroyApiView )
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup', CreateCustomUserApiView.as_view(), name='signup'),
    path('signin', obtain_auth_token, name='signin'),
    path('users', ListCustomUsersApiView.as_view(), name='users'),
    path('complaints', ComplaintListApiView.as_view(), name='complaints'),
    path('complaints/add', ComplaintCreateApiView.as_view(), name='create-complaint'),
    path('complaints/<int:pk>/update', ComplaintUpdateApiView.as_view(), name='update-complaint'),
    path('complaints/<int:pk>/comments', AddCommentApiView.as_view(), name='add-comment'),
    path('complaints/<int:pk>/comments/<int:commentId>/update', UpdateCommentApiView.as_view(), name='update-comment'),
    path('complaints/<int:pk>/comments/<int:commentId>/delete', DestroyCommentApiView.as_view(), name='delete-comment'),
    path('comments', ListCommentApiView.as_view(), name='list-comment'),
    path('address', UserAddressApiView.as_view(), name='address'),
    path('address/<int:pk>/update', UserAddressUpdateApiView.as_view(), name='update-address'),
    path('address/<int:pk>/delete', UserAddressDestroyApiView.as_view(), name='delete-address'),
    path('address/add', UserAddressCreateApiView.as_view(), name='add-address'),
    path('testimonials', UserTestimonialApiView.as_view(), name='testimonial'),
    path('testimonials/add', UserTestimonialCreateApiView.as_view(), name='add-testimonial'),
    path('testimonials/<int:pk>/update', UserTestimonialUpdateApiView.as_view(), name='update-testimonial'),
    path('testimonials/<int:pk>/delete', UserTestimonialDestroyApiView.as_view(), name='delete-testimonial'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
