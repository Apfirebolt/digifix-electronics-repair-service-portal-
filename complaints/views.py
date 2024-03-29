from django.shortcuts import render
from django.views.generic import View, FormView, DetailView, ListView, UpdateView, DeleteView
from .forms import ComplaintImageForm, CreateServiceRequestForm, AddAddressForm, AddCommentForm, TestimonialForm
from django.forms import formset_factory
from .models import ComplaintImages, Complaint, UserAddress, UserTestimonials, Comments
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string


class DetailComplaintView(DetailView):
    model = Complaint
    context_object_name = 'complaint'
    template_name = 'complaints/detail_complaint.html'

    def get_object(self, queryset=None):
        currentObj = super(DetailComplaintView, self).get_object()
        if currentObj.created_by_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj


class UpdateComplaintView(LoginRequiredMixin, UpdateView):
    template_name = 'complaints/update_complaint.html'
    form_class = CreateServiceRequestForm
    model = Complaint

    def get_object(self, queryset=None):
        currentObj = super(UpdateComplaintView, self).get_object()
        if currentObj.created_by_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj

    def form_valid(self, form):
        # perform a action here,
        service_obj = form.save(commit=False)
        service_obj.created_by = self.request.user
        service_obj.save()

        return HttpResponseRedirect(reverse('complaints:complaint_detail', kwargs={'pk': service_obj.pk}))


class CreateComplaintView(LoginRequiredMixin, FormView):
    template_name = 'complaints/create_service_request.html'
    form_class = CreateServiceRequestForm

    def form_valid(self, form):
        # perform a action here,
        service_obj = form.save(commit=False)
        service_obj.created_by = self.request.user
        service_obj.save()

        return HttpResponseRedirect(reverse('complaints:complaint_detail', kwargs={'pk': service_obj.pk}))


@receiver(post_save, sender=Complaint)
def check_if_updated(sender, instance=None, created=False, **kwargs):
    # Check if the object is updated
    if not created:
        complaintInstance = instance
        if complaintInstance.reference_id is None and complaintInstance.status_text:
            complaintInstance.reference_id = get_random_string(8)
            complaintInstance.save()


class AddAddress(LoginRequiredMixin, FormView):
    form_class = AddAddressForm
    template_name = 'complaints/add_address.html'

    def form_valid(self, form):
        # perform a action here,
        address_obj = form.save(commit=False)
        address_obj.owner = self.request.user
        address_obj.save()

        return HttpResponseRedirect(reverse('complaints:all_addresses'))


@receiver(pre_save, sender=UserAddress)
def check_if_primary_address(sender, instance=None, created=False, **kwargs):
    # Check if the added address is used as primary address
    address_instance = instance
    if address_instance.is_primary:
        addresses = UserAddress.objects.filter(owner_id=instance.owner_id).exclude(id=address_instance.id)
        for one_address in addresses:
            one_address.is_primary = False
            one_address.save()


class AllUserAddresses(LoginRequiredMixin, ListView):
    model = UserAddress
    template_name = 'complaints/all_addresses.html'
    context_object_name = 'all_addresses'

    def get_queryset(self):
        qs = UserAddress.objects.filter(owner_id=self.request.user.id)
        return qs


class AllServiceRequests(LoginRequiredMixin, ListView):
    model = Complaint
    template_name = 'complaints/all_requests.html'
    context_object_name = 'all_requests'

    def get_queryset(self):
        qs = Complaint.objects.filter(created_by_id=self.request.user.id)
        return qs


class UpdateAddressView(LoginRequiredMixin, UpdateView):
    model = UserAddress
    template_name = 'complaints/update_address.html'
    form_class = AddAddressForm

    def get_success_url(self):
        return reverse('complaints:all_addresses')

    def get_object(self, queryset=None):
        currentObj = super(UpdateAddressView, self).get_object()
        if currentObj.owner_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj


class DeleteAddressView(LoginRequiredMixin, DeleteView):
    model = UserAddress
    template_name = 'complaints/address_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('complaints:all_addresses')

    def get_object(self, queryset=None):
        currentObj = super(DeleteAddressView, self).get_object()
        if currentObj.owner_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj


class AddRequestImages(FormView):
    ComplaintImageFormSet = formset_factory(
        ComplaintImageForm,
        extra=2,
        max_num=2,
        min_num=1
    )

    template_name = 'complaints/add_complaint_images.html'
    form_class = ComplaintImageFormSet
    success_url = '/'

    def form_valid(self, form):
        for each_form in form:
            cleaned_image_description = each_form.cleaned_data['image_description']
            cleaned_gadget_image = each_form.cleaned_data['gadget_image']
            relatedReqObj = Complaint.objects.get(id=self.kwargs['pk'])
            newRequestImageObj = ComplaintImages(image_description=cleaned_image_description,
                                                 gadget_image=cleaned_gadget_image, related_complaint=relatedReqObj)
            newRequestImageObj.save()
        return HttpResponseRedirect(reverse('complaints:complaint_detail', kwargs={'pk': self.kwargs['pk']}))


class AddNewComment(FormView):
    form_class = AddCommentForm
    template_name = 'complaints/add_comment.html'

    def form_valid(self, form):
        # perform a action here,
        comment_obj = form.save(commit=False)
        comment_obj.written_by = self.request.user
        related_complaint_obj = Complaint.objects.get(id=self.kwargs['pk'])
        comment_obj.related_complaint = related_complaint_obj
        comment_obj.save()

        return HttpResponseRedirect(reverse('complaints:complaint_detail', kwargs={'pk': self.kwargs['pk']}))


class UpdateComment(LoginRequiredMixin, UpdateView):
    model = Comments
    template_name = 'complaints/update_comment.html'
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse_lazy('complaints:complaint_detail', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, queryset=None):
        current_obj = Comments.objects.get(pk=self.kwargs['commentId'])
        if current_obj.written_by.id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return current_obj


class DeleteComment(LoginRequiredMixin, DeleteView):
    model = Comments
    template_name = 'complaints/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('complaints:complaint_detail', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, queryset=None):
        current_obj = Comments.objects.get(pk=self.kwargs['commentId'])
        if current_obj.written_by.id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return current_obj


class CreateTestimonial(FormView):
    """A View to create user testimonial"""
    form_class = TestimonialForm
    template_name = 'complaints/create_testimonial.html'

    def form_valid(self, form):
        # perform a action here,
        testimonialObj = form.save(commit=False)
        testimonialObj.written_by = self.request.user
        testimonialObj.save()

        return HttpResponseRedirect(reverse('complaints:all_testimonials'))


class DeleteTestimonial(DeleteView):
    model = UserTestimonials
    template_name = 'complaints/delete_testimonial_confirm.html'

    def get_success_url(self):
        return reverse_lazy('complaints:all_testimonials')

    def get_object(self, queryset=None):
        currentObj = super(DeleteTestimonial, self).get_object()
        if currentObj.written_by_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj


class ListTestimonials(ListView):
    """A View to list all the testimonials written by users"""

    model = UserTestimonials
    template_name = 'complaints/list_testimonials.html'
    context_object_name = 'testimonials'

    def get_queryset(self):
        qs = UserTestimonials.objects.all()
        return qs


class UpdateTestimonial(UpdateView):
    model = UserTestimonials
    template_name = 'complaints/update_testimonial.html'
    form_class = TestimonialForm

    def get_success_url(self):
        return reverse('complaints:all_testimonials')

    def get_object(self, queryset=None):
        currentObj = super(UpdateTestimonial, self).get_object()
        if currentObj.written_by_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj


class SingleImageDetail(DetailView):
    model = ComplaintImages
    context_object_name = 'complaint_image'
    template_name = 'complaints/image_detail.html'

    def get_object(self, queryset=None):
        currentObj = super(SingleImageDetail, self).get_object()
        if currentObj.related_complaint.created_by_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj


class SingleImageDelete(DeleteView):
    model = ComplaintImages
    template_name = 'complaints/image_delete.html'

    def get_object(self, queryset=None):
        currentObj = super(SingleImageDelete, self).get_object()
        if currentObj.related_complaint.created_by_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj

    def get_success_url(self):
        parentObjId = self.get_object().related_complaint.id
        return reverse_lazy('complaints:complaint_detail', kwargs={'pk': parentObjId})


class SingleImageUpdate(UpdateView):
    model = ComplaintImages
    form_class = ComplaintImageForm
    template_name = 'complaints/image_update.html'

    def get_object(self, queryset=None):
        currentObj = super(SingleImageUpdate, self).get_object()
        if currentObj.related_complaint.created_by_id != self.request.user.id:
            raise Http404("You are not authorized to view this page")
        return currentObj

    def get_success_url(self):
        parentObjId = self.get_object().related_complaint.id
        return reverse('complaints:complaint_detail', kwargs={'pk': parentObjId})


def complaints_view(request):
    return render(request, 'complaints/complaints_home.html', {})
