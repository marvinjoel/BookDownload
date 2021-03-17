from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from apps.bookapp.models import BookModel, CategoryModel


class HomeView(View):

    def get(self, request):
        template = 'home.html'
        backend_books     = BookModel.objects.filter(backend_books=True)
        frontend_books    = BookModel.objects.filter(frontend_books=True)
        datascience_books = BookModel.objects.filter(datascience_books=True)
        return render(request, template, {'backend':backend_books,'frontend':frontend_books,'datascience':datascience_books})

class AllBook_View(View):
    template = 'all_books.html'
    def get(self, request):
        books = BookModel.objects.all()
        return render(request, self.template, {'books':books})


class Category_detail(View):
    template = 'genre_detail.html'
    def get(self, request, slug):
        category = CategoryModel.objects.get(slug=slug)
        return render(request, self.template, dict(category=category))


class BookDetail(View):
    template = 'book_detail.html'
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, pk):
        book = BookModel.objects.get(pk=pk)
        book_category = book.category.first()
        similar_books = BookModel.objects.filter(category__name__startswith=book_category)
        return render(request, self.template, dict(book=book, similar_books=similar_books))



class SearchBook(View):
    template = 'search_book.html'
    def post(self, request):
        search_book = BookModel.objects.filter(title__icontains = request.POST.get('name_of_book'))
        return render(request, self.template,dict(search_book=search_book))

