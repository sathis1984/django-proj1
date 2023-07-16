from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from crudapp.models import Books
from django.urls import reverse_lazy

# Create your views here.
class BookListView(ListView):
    model=Books
    #  context_object_name='books'
    # template_name = 'crudapp/home.html'
    # By default it refers to the books_list.html page under curdadd folder
    # By default it creates the object called books_list and we can refer it in the html page to access the table

class BookDetailView(DetailView):
    model=Books
    # By default it refers to the books_detail.html page under curdadd folder
    # By default it creates the object called books or object and we can refer it in the html page to access the table

class BookCreateView(CreateView):
    model=Books
    fields='__all__'
    # By default it refers to the books_form.html page under curdadd folder

class BookUpdateView(UpdateView):
    model=Books
    fields="__all__"


class BookDeleteView(DeleteView):
    model=Books
    success_url=reverse_lazy('list')
