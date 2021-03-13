from django.shortcuts import render
from django.views import View

from apps.bookapp.models import BookModel


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

