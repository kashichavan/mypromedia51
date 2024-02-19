from django.urls import path
from . import views

urlpatterns = [
    path('studentview/',views.studentview,name='studentview')
]
