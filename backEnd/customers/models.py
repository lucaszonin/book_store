from django.db import models
from django.template.defaultfilters import slugify

from curvas.models import Curva
# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=128)
    slug = models.SlugField(null=True, blank=True)
    curva = models.ForeignKey(Curva, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = slugify(self.name)

        super(Customer, self).save(*args, **kwargs)