from django.shortcuts import render,redirect
from .models import dataentry
from .models import item

# Create your views here.

def index(request):
    return render(request, 'index.html')

def stretching(request):
    return render(request,'stretching.html')    


def search(request):
    name= request.GET.get('search')
    if name:
        datas=dataentry.objects.filter(categ__icontains=name) or dataentry.objects.filter(name__icontains=name)
        print(datas)
        return render(request,'search_result.html',{'datas': datas , 'name': name} )

    else:
        return redirect('index')


def bodybuild(request):
    datas=dataentry.objects.filter(categ__icontains="bodybuilding")
    return render(request,'stretching.html',{'datas':datas})


def cardio(request):
    datas=dataentry.objects.filter(categ__icontains="cardio")
    return render(request,'stretching.html',{'datas':datas})

def chest(request):
    datas= item.objects.filter(categ__icontains="chest")
    return render(request,'workouts/content.html',{'datas':datas})


def biceps(request):
    datas= item.objects.filter(categ__icontains="biceps")
    return render(request,'workouts/content.html',{'datas':datas})


def triceps(request):
    datas= item.objects.filter(categ__icontains="triceps")
    return render(request,'workouts/content.html',{'datas':datas})


















