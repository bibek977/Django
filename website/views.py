from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data={'title':'HomePage'}
    return render(request, 'index.html',data)

def features(request):
    return HttpResponse("<h1>Feature Page</h1>")

def contact(request):
    return render(request, 'contact.html')
    
def about(request):
    phoneNumber = request.GET.get('number','98000000')
    print(phoneNumber)
    return HttpResponse("<h1>About Page</h1> <br>" + phoneNumber)

