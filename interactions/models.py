from django.conf import settings
from django.db import models
from listings.models import Property
class VisitRequest(models.Model):
 class Status(models.TextChoices):
  PENDING='pending','Pending'
  ACCEPTED='accepted','Accepted'
  REJECTED='rejected','Rejected'
  COMPLETED='completed','Completed'
 student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='visit_requests'); property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='visits'); requested_for=models.DateTimeField(); status=models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING); note=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True)
 def __str__(self): return f'Visit: {self.student} → {self.property}'
class Inquiry(models.Model):
 student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='inquiries'); property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='inquiries'); message=models.TextField(); created_at=models.DateTimeField(auto_now_add=True); is_read=models.BooleanField(default=False)
class ChatMessage(models.Model):
 inquiry=models.ForeignKey(Inquiry,on_delete=models.CASCADE,related_name='messages'); sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); body=models.TextField(); sent_at=models.DateTimeField(auto_now_add=True)
class Review(models.Model):
 property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='reviews'); author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); rating=models.PositiveSmallIntegerField(); body=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True)
