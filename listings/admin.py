from django.contrib import admin
from .models import Property,Room,Amenity,ListingImage
admin.site.register([Property,Room,Amenity,ListingImage])
