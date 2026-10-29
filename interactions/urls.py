from django.urls import path
from . import views
app_name='interactions'
urlpatterns=[path('visit/<int:pk>/',views.request_visit,name='request_visit'),path('visits/',views.student_visits,name='student_visits'),path('owner/',views.owner_dashboard,name='owner_dashboard'),path('visit/<int:pk>/<str:status>/',views.update_visit,name='update_visit'),path('contact/<int:pk>/',views.contact_owner,name='contact_owner')]
