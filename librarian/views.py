from django.shortcuts import render

class Viewbook(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
class Addbook(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ['title', 'author', 'category', 'published_date']
    success_url = reverse_lazy('book_list')
class Editbook(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    fields = ['title', 'author', 'category', 'published_date']
    success_url = reverse_lazy('book_list')
class Deletebook(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('book_list')
    
