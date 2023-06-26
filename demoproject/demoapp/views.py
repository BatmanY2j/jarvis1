from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    num=Team.objects.all()

    return render(request,"index.html",{'result':obj,'out':num})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     a=x-y
#     b=x*y
#     c=x/y
#
#     return render(request,"result.html",{'lol':res,'l1':a,'l2':b,'l3':c})