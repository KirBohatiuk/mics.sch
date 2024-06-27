from django.urls import path

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('assign-lesson', views.assign_lesson, name='assign-lesson'),
    path('blog', views.blog, name='blog'),
]
