from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'app/login.html', {'title': 'Login'}) # request, html path, title
