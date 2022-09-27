from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('portfolio',PortfolioView.as_view(),name='portfolio'),
    path('detail/<int:pk>',DetailView.as_view(),name='detail'),
    path('change_lang',change_lang, name="change_lang" ),

    
]

