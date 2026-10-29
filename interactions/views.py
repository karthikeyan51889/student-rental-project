from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect
from listings.models import Property
from .models import VisitRequest,Inquiry
@login_required
def request_visit(request,pk):
 prop=get_object_or_404(Property,pk=pk,is_published=True)
 if request.method=='POST':
  VisitRequest.objects.create(student=request.user,property=prop,requested_for=request.POST.get('requested_for'),note=request.POST.get('note','')); return redirect('interactions:student_visits')
 return render(request,'interactions/request_visit.html',{'property':prop})
@login_required
def student_visits(request): return render(request,'interactions/student_visits.html',{'visits':VisitRequest.objects.filter(student=request.user).select_related('property')})
@login_required
def owner_dashboard(request): return render(request,'interactions/owner_dashboard.html',{'visits':VisitRequest.objects.filter(property__owner=request.user).select_related('property','student')})
@login_required
def update_visit(request,pk,status):
 visit=get_object_or_404(VisitRequest,pk=pk,property__owner=request.user)
 if request.method=='POST' and status in ('accepted','rejected'): visit.status=status; visit.save(update_fields=['status'])
 return redirect('interactions:owner_dashboard')
@login_required
def contact_owner(request,pk):
 prop=get_object_or_404(Property,pk=pk,is_published=True)
 if request.method=='POST': Inquiry.objects.create(student=request.user,property=prop,message=request.POST.get('message','')); return redirect('interactions:student_visits')
 return render(request,'interactions/contact_owner.html',{'property':prop})
