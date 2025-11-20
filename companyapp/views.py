from django.shortcuts import render

from companyapp.models import About, Slider

# Create your views here.
def homefunction(request):
    sliders = Slider.objects.all()
    about = About.objects.get(id=1)  # Retourne None si n'existe pas
    context = {
        'sliders': sliders,
        'about': about,
    }
    return render(request, 'companyapp/index.html', context)
