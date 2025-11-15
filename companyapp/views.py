from django.shortcuts import render

# Create your views here.
def homefunction(request):
    return render(request, 'companyapp/index.html')