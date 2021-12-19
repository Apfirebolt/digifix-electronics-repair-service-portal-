from django.urls import path
from django.conf.urls.static import static
from digifix_computer_repair import settings
from . views import ( UserAddressApiView, UserTestimonialApiView, CreateCustomUserApiView, ListCustomUsersApiView,
                      ComplaintListApiView, ComplaintCreateApiView, ComplaintUpdateApiView,
                      ReportIssueCreateApiView, ReportIssueUpdateApiView, DestroyReportIssueApiView,
                      ListReportIssueApiView,  AddCommentApiView, UpdateCommentApiView, DestroyCommentApiView,
                      ListCommentApiView, AddComplaintImageApiView, UpdateComplaintImageApiView,
                      DestroyComplaintImageApiView, ListComplaintImagesApiView, UserAddressCreateApiView,
                      UserAddressDestroyApiView, UserAddressUpdateApiView, UserTestimonialCreateApiView,
                      UserTestimonialUpdateApiView, UserTestimonialDestroyApiView,
                      ChangeSettingsApiView )
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup', CreateCustomUserApiView.as_view(), name='signup'),
    path('signin', obtain_auth_token, name='signin'),
    path('settings', ChangeSettingsApiView.as_view(), name='settings'),
    path('users', ListCustomUsersApiView.as_view(), name='users'),
    path('complaints', ComplaintListApiView.as_view(), name='complaints'),
    path('complaints/add', ComplaintCreateApiView.as_view(), name='create-complaint'),
    path('complaints/<int:pk>/update', ComplaintUpdateApiView.as_view(), name='update-complaint'),
    path('complaints/<int:pk>/issues/add', ReportIssueCreateApiView.as_view(), name='add-issues'),
    path('complaints/<int:pk>/issues/<int:issueId>/update', ReportIssueUpdateApiView.as_view(), name='update-issue'),
    path('complaints/<int:pk>/issues/<int:issueId>/delete', DestroyReportIssueApiView.as_view(), name='delete-issue'),
    path('issues', ListReportIssueApiView.as_view(), name='list-issues'),
    path('complaints/<int:pk>/images', AddComplaintImageApiView.as_view(), name='add-images'),
    path('complaints/<int:pk>/images/<int:imageId>/update', UpdateComplaintImageApiView.as_view(), name='update-image'),
    path('complaints/<int:pk>/images/<int:imageId>/delete', DestroyComplaintImageApiView.as_view(), name='delete-image'),
    path('images', ListComplaintImagesApiView.as_view(), name='list-images'),
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
