from django.shortcuts import render
from . models import Place,Partner
# Create your views here.
def demo(request):
   obj=Place.objects.all()
   obje=Partner.objects.all()
   return render (request,"index.html",{'result':obj,'results':obje})


