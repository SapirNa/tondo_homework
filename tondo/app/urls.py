from django.urls import path
from .views import get_details, save_details

urlpatterns =[
    path('data/<int:userid>', get_details, name='get_details'),
    path('data/save/<int:userid>', save_details, name='save_details')
]
