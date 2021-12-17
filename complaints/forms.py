from django import forms
from . models import Complaint, ComplaintImages, UserAddress, Comments, UserTestimonials
from django.core.validators import FileExtensionValidator
from . models import DEVICE_TYPE_CHOICES

class CreateServiceRequestForm(forms.ModelForm):
  description = forms.CharField(label=("Please Enter Description"),
                             widget=forms.Textarea(attrs={'class': 'form-control'}))
  device_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=DEVICE_TYPE_CHOICES)
  class Meta:
    model = Complaint
    fields = ('description', 'device_type',)


class ComplaintImageForm(forms.ModelForm):
  gadget_image = forms.FileField(label=("Please Upload Your Gadget Image"),
                                  widget=forms.FileInput, validators=[FileExtensionValidator(['png', 'jpg'])])
  image_description = forms.CharField(label=("Please Enter Image Description"),
                             widget=forms.Textarea(attrs={'class': 'my-3 appearance-none roundedoutline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))

  class Meta:
    model = ComplaintImages
    fields = ('gadget_image', 'image_description',)


class AddAddressForm(forms.ModelForm):
  address = forms.CharField(label="Add Address", widget=forms.Textarea(attrs={'class': 'form-control'}))
  is_primary = forms.CheckboxInput()

  class Meta:
    model = UserAddress
    fields = ('address', 'is_primary',)


class AddCommentForm(forms.ModelForm):
  description = forms.CharField(label="Add Comment", widget=forms.Textarea)

  class Meta:
    model = Comments
    fields = ('description',)


class TestimonialForm(forms.ModelForm):

  class Meta:
    model = UserTestimonials
    fields = ('content', 'service_rating',)