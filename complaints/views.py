from django.shortcuts import render
from django.views.generic import View, FormView, DetailView, ListView, UpdateView, DeleteView
from . forms import Complaint, ComplaintImageForm, CreateServiceRequestForm, AddAddressForm, AddCommentForm
from django.forms import modelformset_factory
from . models import ComplaintImages, Complaint, UserAddress
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin


class DetailComplaintView(DetailView):
  model = Complaint
  context_object_name = 'complaint'
  template_name = 'complaints/detail_complaint.html'


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


class AddAddress(LoginRequiredMixin, FormView):
  form_class = AddAddressForm
  template_name = 'complaints/add_address.html'

  def form_valid(self, form):
    # perform a action here,
    address_obj = form.save(commit=False)
    address_obj.owner = self.request.user
    address_obj.save()

    return HttpResponseRedirect(reverse('complaints:all_addresses'))


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


class AddRequestImages(View):

  def get(self, request, pk):
    ComplaintImageFormSet = modelformset_factory(ComplaintImages,
                                        ComplaintImageForm, extra=2)
    return render(request, 'complaints/add_complaint_images.html', {
      'image_formset': ComplaintImageFormSet
    })

  def post(self, request):
    print(request.POST)
    print(request.FILES)
    return HttpResponse('Done this time')


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




def complaints_view(request):
  return render(request, 'complaints/complaints_home.html', {})


