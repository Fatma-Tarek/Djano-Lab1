from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book

# Create your views here.
#request mandatory 
def index(request):
    books = Book.objects.all() #fetch all books
    #same as html but I don't write html in view 
    #return HttpResponse("Hello from books")
    return render(request,"books/index.html",{
        "books" : books
    })

def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request,"books/create.html",{
        "form" : form
    })



