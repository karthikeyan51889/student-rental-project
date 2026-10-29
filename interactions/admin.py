from django.contrib import admin
from .models import VisitRequest,Inquiry,ChatMessage,Review
admin.site.register([VisitRequest,Inquiry,ChatMessage,Review])
