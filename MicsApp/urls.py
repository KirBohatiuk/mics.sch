from django.urls import path

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact-info', views.contact_info, name='contact-info')
]
