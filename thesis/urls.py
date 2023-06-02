from django.urls import path
from .views import index, convert_to_braille_image, translate

# urlconf
urlpatterns = [
    path('', index, name="index"),
    path('braille/', convert_to_braille_image, name='braille'),
    path('translate/', translate, name='translate')
]
