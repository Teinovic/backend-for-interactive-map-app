from django.db import models


class InteractiveMap(models.Model):
   coordinates = models.CharField(max_length=100)
   type_of_poison = models.TextField()
   cleared = models.BooleanField(default=False)

   def _str_(self):
     return self.coordinates