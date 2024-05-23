from django import forms
from .models import *

class AddCategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['name','amount']


class UpdateCategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['name','amount']


class AddRoomForm(forms.ModelForm):
  class Meta:
    model = Room
    exclude = ('is_available',)


class UpdateRoomForm(forms.ModelForm):
  class Meta:
    model = Room
    exclude = ('is_available',)


class NewBookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    exclude = ('room',)



class UpdateBookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    exclude = ('room',)