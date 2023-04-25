from django.urls import path
from .views import index, convert_text_to_braille, convert_to_braille_image

# urlconf
urlpatterns = [
    path('', index, name="index"),
    path('convert_text_to_braille/', convert_text_to_braille, name='convert_text_to_braille'),
    path('braille/', convert_to_braille_image, name='braille')
]