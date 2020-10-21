from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Curva(models.Model):

    name = models.CharField(max_length=128)
    slug = models.SlugField(null=True, blank=True)
    coeficiente = models.FloatField()


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = slugify(self.name)

        super(Curva, self).save(*args, **kwargs)