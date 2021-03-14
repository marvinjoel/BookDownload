from django.urls import path

from apps.bookapp.views import HomeView, AllBook_View, Category_detail, BookDetail  # , BookDetail

app_name = 'book'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('all_books/', AllBook_View.as_view(), name='book_all'),
    path('genre/<str:slug>/', Category_detail.as_view(), name='category_detail'),
    path('<int:pk>/', BookDetail.as_view(), name='book_detail'),
]