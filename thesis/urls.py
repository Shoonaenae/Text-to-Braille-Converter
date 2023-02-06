from django.urls import path
from .views import index

# urlconf
urlpatterns = [
    path('ocr/', index, name="index")
]