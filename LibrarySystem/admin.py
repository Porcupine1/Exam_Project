from django.contrib import admin
from .models import HardBook, SoftBook, Borrower

admin.site.register(HardBook)
admin.site.register(SoftBook)
admin.site.register(Borrower)
