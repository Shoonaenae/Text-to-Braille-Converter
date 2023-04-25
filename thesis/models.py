from django.db import models

# Create your models here.

class BrailleImages(models.Model):
    input_text = models.CharField(max_length=255)
    braille_text = models.CharField(max_length=255)
    image_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    class meta: 
       db_table = 'braille_images'