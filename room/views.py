from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


# Create your views here.
@login_required
def add_category(request):
  categories = Category.objects.all().order_by('-id')
  if request.POST:
    form = AddCategoryForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'New category added to manage rooms')
      return redirect('add_category')
    else:
      messages.warning(request,'Error Try Again...')
      return redirect('add_category')
  else:
    form = AddCategoryForm()
  return render(request,'add_category.html',{'form':form,'categories':categories})


@login_required
def update_category(request,pk):
  category = Category.objects.get(id=pk)
  if request.POST:
    form = UpdateCategoryForm(request.POST,instance=category)
    if form.is_valid():
      form.save()
      messages.success(request,'New category added to manage rooms')
      return redirect('update_category', category.id)
    else:
      messages.warning(request,'Error Try Again...')
      return redirect('update_category', category.id)
  else:
    form = UpdateCategoryForm(instance=category)
  return render(request,'update_category.html',{'form':form})



def delete_category(request,pk):
  category = Category.objects.get(id=pk)
  category.delete()
  messages.success(request,'Category Deleted Successfully...')
  return redirect('dashboard')


@login_required
def add_room(request):
  rooms = Room.objects.all().order_by('-id')[:5]
  if request.POST:
    form = AddRoomForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'New Room added Successfully..')
      return redirect('add_room')
    else:
      messages.warning(request,'Error Try Again...')
      return redirect('add_room')
  else:
    form = AddRoomForm()
  return render(request,'add_room.html',{'form':form,'rooms':rooms})


@login_required
def update_room(request,pk):
  room = Room.objects.get(id=pk)
  rooms = Room.objects.all().order_by('-id')[:5]
  if request.POST:
    form = UpdateRoomForm(request.POST,instance=room)
    if form.is_valid():
      form.save()
      messages.success(request,'Update room Successfully..')
      return redirect('update_room', room.id)
    else:
      messages.warning(request,'Error Try Again...')
      return redirect('update_room', room.id)
  else:
    form = UpdateRoomForm(instance=room)
  return render(request,'update_room.html',{'form':form,'rooms':rooms})


def all_rooms(request):
  rooms = Room.objects.all().order_by('-id')
  return render(request,'all_rooms.html',{'rooms':rooms})


def delete_room(request,pk):
  room = Room.objects.get(id=pk)
  room.delete()
  messages.success(request,'Deleted Successfully..')
  return redirect('all_rooms')




def new_booking(request,pk):
  room = Room.objects.get(id=pk)
  if request.POST:
    form = NewBookingForm(request.POST)
    if form.is_valid():
      new = form.save(commit=False)
      new.room = room
      room.is_available = False
      new.save()
      room.save()
      messages.success(request,'New Booking has been successfully..')
      return redirect('dashboard')
    else:
      messages.warning(request,'Error Try agin!!!')
      return redirect('new_booking', room.id)
  else:
    form = NewBookingForm()
  return render(request,'new_booking.html',{'form':form,'room':room})



def update_booking(request,pk):
  booking = Booking.objects.get(id=pk)
  if request.POST:
    form = UpdateBookingForm(request.POST,instance=booking)
    if form.is_valid():
      form.save()
      messages.success(request,'Update Booking has been successfully..')
      return redirect('dashboard')
    else:
      messages.warning(request,'Error Try agin!!!')
      return redirect('new_booking', booking.id)
  else:
    form = UpdateBookingForm(instance=booking)
  return render(request,'update_booking.html',{'form':form,'booking':booking})




def checkout_guest(request,pk):
  bookign = Booking.objects.get(id=pk)
  bookign.checked_out = True

  room = Room.objects.get(id=bookign.room.pk)
  room.is_available = True
  room.save()
  bookign.save()
  messages.success(request,'Guest has been checked out and room is new available for use.')
  return redirect('dashboard')



def guest_history_per_room(request,pk):
  room = Room.objects.get(pk=pk)
  guests = room.booking_set.all().order_by('-id')
  return render(request,'guest_history_per_room.html',{'guests':guests})



def all_active_guests(request):
  guests = Booking.objects.filter(checked_out=False)
  return render(request,'all_active_guests.html',{'guests':guests})

def active_guests_per_room(request,pk):
  room = Room.objects.get(id=pk)
  guests = room.booking_set.all()
  return render(request,'active_guests_per_room.html',{'guests':guests})
