from datetime import timezone
from django.shortcuts import redirect, render
from django.views.generic import  CreateView
from .models import SoftBook, HardBook
from .forms import SoftBookForm
from django.contrib import messages
from django.urls import reverse_lazy
import datetime



def home(request):
    latestHardBook = HardBook.objects.order_by('-pub_date')[:4]
    latestSoftBook = SoftBook.objects.order_by('-pub_date')[:4]
    context = {
        'latestHardBook' : latestHardBook,
        'latestSoftBook' : latestSoftBook
    }
    return render(request, 'LibrarySystem/home.html', context)

def aboutUs(request):
    return render(request, 'LibrarySystem/aboutUs.html')

def preview(request, book_id):
    book = SoftBook.objects.get(id=book_id)
    print(book.book.path)
    return render(request, 'LibrarySystem/preview.html',{'book':book})

class BookCreateView(CreateView):
    model = SoftBook
    form_class = SoftBookForm
    template_name = 'LibrarySystem/softbook_form.html'

    def get_context_data(self,**kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        context['softbooks'] = SoftBook.objects.all()
        context['hardbooks'] = HardBook.objects.all()
        return context
    
    def get_success_url(self):
        return redirect(reverse_lazy('LibrarySystem:BookCreateView'))

    def post(self, request):
        form = SoftBookForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Sccessfully added {} to the Library.'.format(request.POST['title']))
            return redirect(reverse_lazy('LibrarySystem:BookCreateView'))
