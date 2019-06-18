from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def dashboard(request):
    return HttpResponse("<h1>welcome to django</h1>")
def login(request):
    t = get_template('login.html')
    html = t.render()
    return HttpResponse(html)