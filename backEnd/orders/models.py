from django.db import models

from customers.models import Customer
from books.models import Book
# Create your models here.
class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_quantity = models.PositiveIntegerField(default=1)
    is_paid = models.BooleanField(default=True)
    date = models.DateField()



class OrderItem(models.Model):

    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)

    def __str__(self):
        
        return f'{self.book.name}'