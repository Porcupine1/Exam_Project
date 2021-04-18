from django.urls import path
from . import views

app_name = 'LibrarySystem'

urlpatterns = [
     path('', views.home, name='home'),
     path('books/', views.BookCreateView.as_view(), name='BookCreateView'),
     path('books/preview/<book_id>', views.preview, name='preview'),
     path('about', views.aboutUs, name='aboutUs'),
]
