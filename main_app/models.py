from django.db import models

# Create your models here.

# The Widget Model only has two fields:
# description - a CharField with a max_length of your choosing
# quantity - an IntegerField

class Widget(models.Model):
    desciption = models.CharField(max_length=200)
    quantity = models.IntegerField()



