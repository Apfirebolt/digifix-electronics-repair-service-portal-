from django.urls import path, include
from django.conf.urls.static import static
from digifix_computer_repair import settings
from . views import ( complaints_view, CreateComplaintView, DetailComplaintView, AddAddress,
                      AllUserAddresses, AllServiceRequests, UpdateAddressView, DeleteAddressView
                      ,UpdateComplaintView, AddRequestImages, AddNewComment, CreateTestimonial, UpdateTestimonial,
                      ListTestimonials, DeleteTestimonial, SingleImageDelete, SingleImageUpdate, SingleImageDetail )


urlpatterns = [
    path('', complaints_view, name='home'),
    path('create', CreateComplaintView.as_view(), name='create_request'),
    path('add_address', AddAddress.as_view(), name='add_address'),
    path('all_addresses', AllUserAddresses.as_view(), name='all_addresses'),
    path('all_requests', AllServiceRequests.as_view(), name='all_requests'),
    path('add_images/<int:pk>', AddRequestImages.as_view(), name='add_images'),
    path('add_comment/<int:pk>', AddNewComment.as_view(), name='add_comment'),
    path('detail/<int:pk>', DetailComplaintView.as_view(), name='complaint_detail'),
    path('request/update/<int:pk>', UpdateComplaintView.as_view(), name='complaint_update'),
    path('update/<int:pk>', UpdateAddressView.as_view(), name='address_update'),
    path('delete/<int:pk>', DeleteAddressView.as_view(), name='address_delete'),
    path('testimonials', ListTestimonials.as_view(), name='all_testimonials'),
    path('create_testimonial', CreateTestimonial.as_view(), name='create_testimonial'),
    path('update_testimonial/<int:pk>', UpdateTestimonial.as_view(), name='update_testimonial'),
    path('delete_testimonial/<int:pk>', DeleteTestimonial.as_view(), name='delete_testimonial'),
    path('image_delete/<int:pk>', SingleImageDelete.as_view(), name='image_delete'),
    path('image_update/<int:pk>', SingleImageUpdate.as_view(), name='image_update'),
    path('image_detail/<int:pk>', SingleImageDetail.as_view(), name='image_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
