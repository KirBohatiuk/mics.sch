from django.urls import path

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact-info', views.contact_info, name='contact-info'),
    path('assign-lesson', views.assign_lesson, name='assign-lesson'),
    path('blog', views.blog, name='blog'),
]
