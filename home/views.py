from django.shortcuts import render,redirect


def home(request):
    return render(request,'home.html')


def play(request,room_code):
    return render(request,'play.html',context)

