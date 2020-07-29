from django import forms
from . models import Complaint, ComplaintImages, UserAddress, Comments, UserTestimonials
from django.core.validators import FileExtensionValidator


class CreateServiceRequestForm(forms.ModelForm):

  class Meta:
    model = Complaint
    fields = ('description', 'device_type',)


class ComplaintImageForm(forms.ModelForm):
  gadget_image = forms.FileField(label=("Please Upload Your Gadget Image"),
                                  widget=forms.FileInput, validators=[FileExtensionValidator(['png', 'jpg'])])
  image_description = forms.CharField(label=("Please Enter Image Description"),
                             widget=forms.Textarea)

  class Meta:
    model = ComplaintImages
    fields = ('gadget_image', 'image_description',)


class AddAddressForm(forms.ModelForm):
  address = forms.CharField(label="Add Address", widget=forms.Textarea)
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