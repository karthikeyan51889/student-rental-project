from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404,render,redirect
from .forms import PropertyForm,RoomForm
from .models import Property

def home(request): return render(request,'listings/home.html')
def listing_list(request):
 qs=Property.objects.filter(is_published=True,rooms__is_occupied=False).distinct().prefetch_related('rooms','amenities','images')
 area=request.GET.get('area',''); budget=request.GET.get('max_rent',''); room_type=request.GET.get('room_type','')
 if area: qs=qs.filter(Q(area__icontains=area)|Q(city__icontains=area))
 if budget.isdigit(): qs=qs.filter(rooms__rent__lte=int(budget))
 if room_type: qs=qs.filter(rooms__room_type=room_type)
 return render(request,'listings/listing_list.html',{'properties':qs.distinct(),'area':area,'max_rent':budget,'room_type':room_type})
def listing_detail(request,pk): return render(request,'listings/listing_detail.html',{'property':get_object_or_404(Property.objects.prefetch_related('rooms','amenities','images'),pk=pk,is_published=True)})
@login_required
def add_listing(request):
 if request.user.role!='owner': return redirect('listings:home')
 form=PropertyForm(request.POST or None); rf=RoomForm(request.POST or None)
 if request.method=='POST' and form.is_valid() and rf.is_valid():
  prop=form.save(commit=False); prop.owner=request.user; prop.save(); form.save_m2m(); room=rf.save(commit=False); room.property=prop; room.save(); return redirect('listings:detail',pk=prop.pk)
 return render(request,'listings/add_listing.html',{'form':form,'room_form':rf})
