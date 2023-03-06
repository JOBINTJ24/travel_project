from django.http import HttpResponse
from django.shortcuts import render
from .models import place
# Create your views here.
def demo(request):
      obj=place.objects.all()
      return render(request,"index.html",{'result':obj})
# def addition(request):
#        x=int(request.GET['num1'])
#        y=int(request.GET['num2'])
#        res1=x+y
#        res2=x-y
#        res3=x*y
#        res4=x/y
#        return render(request,"about.html",{'result': res1,'result1':res2,'result2':res3,'result3':res4})
