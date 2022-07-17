from django.shortcuts import render,HttpResponse

# Create your views here.

## Home function
def home(request):
    return render(request,'Home/home.html')