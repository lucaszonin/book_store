from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from django.contrib.auth.models import User
from authors.models import Author
from categories.models import Category

# Create your models here.
class Book(models.Model):

    name = models.CharField(max_length=128)
    img = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number_pages = models.IntegerField()
    year = models.IntegerField()
    cost_price = models.FloatField()
    slug = models.SlugField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = slugify(self.name)

        super(Book, self).save(*args, **kwargs)