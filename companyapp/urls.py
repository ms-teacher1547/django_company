from django.urls import include, path

from companyapp import views


urlpatterns = [
    path('', views.homefunction, name='homeapp'),
]
