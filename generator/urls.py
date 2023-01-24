from django.urls import path
from .views import get_screenshot

app_name = 'generator'

urlpatterns = [
    path('', get_screenshot, name='get_screen'),
]