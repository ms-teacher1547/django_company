from django.shortcuts import render

from companyapp.models import Slider

# Create your views here.
def homefunction(request):
    sliders = Slider.objects.all()
    context = {'sliders': sliders}
    return render(request, 'companyapp/index.html', context)
