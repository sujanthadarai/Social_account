from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def log_in(request):
    return render(request,'login.html')

