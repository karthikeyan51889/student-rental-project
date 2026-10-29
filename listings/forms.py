from django import forms
from .models import Property,Room
class PropertyForm(forms.ModelForm):
 class Meta: model=Property; fields=('title','description','area','city','address','amenities')
class RoomForm(forms.ModelForm):
 class Meta: model=Room; fields=('room_type','rent','deposit','bedrooms','bathrooms','available_from')
