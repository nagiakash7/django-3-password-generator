from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


#information regarding the home page 
# def home(request):
#     return render(request,'generator/home.html')

#how to pass a dictionary value
def home(request):
    return render(request,'generator/home.html')


#information regarding the eggs page 
# def eggs(request):
#     return HttpResponse('Hello there eggs here ')

def password(request):
    # return HttpResponse('Hello there password here ')
    characters=list('abcdefghijkjlmnopqrstuvwxyz')


    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%^&*('))

    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
