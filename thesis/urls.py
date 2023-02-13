from django.urls import path
from .views import index

# urlconf
urlpatterns = [
    path('', index, name="index")
]