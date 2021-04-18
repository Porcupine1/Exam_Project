from django.db import models
from django.utils import timezone
import datetime

class Book(models.Model):
    title = models.CharField('Book Title', max_length=200, null=False)
    image = models.ImageField('Book Cover', upload_to='covers', null=False)
    genre = models.CharField('Genre', max_length= 350, null=False)
    pub_date = models.DateTimeField('Date Published', auto_now_add=True, null=False)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    
    def __str__(self):
        return self.title   


class SoftBook(Book):
    book = models.FileField('Book',upload_to='books', null=False)

class HardBook(Book):
    quantity = models.IntegerField('Quantity')

class Borrower(models.Model):
    name = models.CharField('Name', max_length=100)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    returned = models.BooleanField(null=True)

    def __str__(self):
        return self.name