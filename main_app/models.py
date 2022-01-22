from django.db import models
from django.urls import reverse

# Create your models here.

# The Widget Model only has two fields:
# description - a CharField with a max_length of your choosing
# quantity - an IntegerField

class Widget(models.Model):
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse('index')  




