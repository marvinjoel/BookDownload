from django.urls import path

from apps.bookapp.views import HomeView, AllBook_View

app_name = 'book'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('all_books/', AllBook_View.as_view(), name='book_all'),
]