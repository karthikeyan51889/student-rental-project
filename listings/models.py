from django.conf import settings
from django.db import models
class Amenity(models.Model):
 name=models.CharField(max_length=60,unique=True)
 def __str__(self): return self.name
class Property(models.Model):
 owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='properties')
 title=models.CharField(max_length=140); description=models.TextField(); area=models.CharField(max_length=100,db_index=True); address=models.CharField(max_length=240,blank=True); city=models.CharField(max_length=80,blank=True)
 amenities=models.ManyToManyField(Amenity,blank=True,related_name='properties')
 is_published=models.BooleanField(default=True); created_at=models.DateTimeField(auto_now_add=True)
 def __str__(self): return self.title
class Room(models.Model):
 class RoomType(models.TextChoices):
  SINGLE='single','Single'
  SHARED='shared','Shared'
  STUDIO='studio','Studio'
 property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='rooms')
 room_type=models.CharField(max_length=10,choices=RoomType.choices,default=RoomType.SINGLE)
 rent=models.PositiveIntegerField(); deposit=models.PositiveIntegerField(default=0); available_from=models.DateField(null=True,blank=True); is_occupied=models.BooleanField(default=False); bedrooms=models.PositiveSmallIntegerField(default=1); bathrooms=models.PositiveSmallIntegerField(default=1)
 def __str__(self): return f'{self.property.title} — {self.get_room_type_display()}'
class ListingImage(models.Model):
 property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='images')
 image=models.ImageField(upload_to='listings/'); caption=models.CharField(max_length=120,blank=True); uploaded_at=models.DateTimeField(auto_now_add=True)
