from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('events/', views.events, name='events'),
    path('projects/', views.projects, name='projects'),
    path('gallery/', views.gallery, name='gallery'),
    path('achievements/', views.achievements, name='achievements'),
    path('calendar/', views.calendar, name='calendar'),
    path('magazine/',views.magazine, name= 'magazine'),
    path('mentor/',views.mentor, name= 'mentor'),
    path('alumni/',views.alumni, name= 'alumni'),
]
