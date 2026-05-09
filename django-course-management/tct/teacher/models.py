from django.db import models


class Teacher(models.Model):
   def __init__(self, *args, **kwargs):
       super().__init__(args, kwargs)
       self.courses = None

   name = models.CharField(max_length=100)
   email = models.EmailField(unique=True)