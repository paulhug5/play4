from django.shortcuts import render

# Create your views here.

#home
def home(request):
    return render(request, 'main/home.html')