from django.urls import path
from . import views



urlpatterns = [
    path('create/', views.get_name,name="create" ),
   
   
 
]