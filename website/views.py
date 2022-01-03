from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Django project</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")