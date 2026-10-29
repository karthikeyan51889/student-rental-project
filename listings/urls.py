from django.urls import path
from . import views
app_name='listings'
urlpatterns=[path('',views.home,name='home'),path('listings/',views.listing_list,name='list'),path('listings/add/',views.add_listing,name='add'),path('listings/<int:pk>/',views.listing_detail,name='detail')]
