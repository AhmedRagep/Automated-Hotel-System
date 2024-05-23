from django.urls import path
from .views import *

urlpatterns = [
  path('add_category',add_category,name='add_category'),
  path('update_category/<int:pk>',update_category,name='update_category'),
  path('delete_category/<int:pk>',delete_category,name='delete_category'),
  
  # Room
  path('add_room',add_room,name='add_room'),
  path('all_rooms',all_rooms,name='all_rooms'),
  path('update_room/<int:pk>',update_room,name='update_room'),
  path('delete_room/<int:pk>',delete_room,name='delete_room'),

  # Booking
  path("new_booking/<int:pk>", new_booking, name="new_booking"),
  path("update_booking/<int:pk>", update_booking, name="update_booking"),

  # Checked Out
  path("checkout_guest/<int:pk>", checkout_guest, name="checkout_guest"),
  
  # History
  path("guest_history_per_room/<int:pk>", guest_history_per_room, name="guest_history_per_room"),
  path("all_active_guests", all_active_guests, name="all_active_guests"),
  path("acactive_guests_per_room/<int:pk>",active_guests_per_room, name="acactive_guests_per_room"),

]