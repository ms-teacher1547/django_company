from django.shortcuts import render

from .models import About, Portfolio, Service, Slider

# Create your views here.
def homefunction(request):
    sliders = Slider.objects.all()
    about = About.objects.get(id=1)  # Retourne None si n'existe pas
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    context = {
        'sliders': sliders,
        'about': about,
        'services': services,
        'portfolios': portfolios,
    }
    return render(request, 'companyapp/index.html', context)
