from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.

def fun_bv(request):
    return HttpResponse ('fun_bv created')

class cls_bv(View):
    def get(self,request):

        return HttpResponse('cls_bv created')
    

def fbv_html(request):
    return render(request,'fbv_html.html')
    

class Cbv_html(View):
    def get(self,request):
        return render(request,'Cbv_html.html')
    


def insert_school_fbv(request):
    SFO=Schoolform()
    d={'SFO':SFO}

    if request.method=='POST':

        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()

            return HttpResponse('insert_school_fbv created')


    return render(request,'insert_school_fbv.html',d)

class Insert_School_Cbv(View):
    def get(self,request):
        ESFO=Schoolform()
        d={'ESFO':ESFO}
        return render(request,'Insert_School_Cbv.html',d)
    
    def post(self,request):
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByCbv is done')
        


class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'






