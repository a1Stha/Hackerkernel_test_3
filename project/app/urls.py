from django.urls import path
from . import views

urlpatterns = [
    path('add_author/', views.add_author, name='add_author'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_borrow_record/', views.add_borrow_record, name='add_borrow_record'),
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('borrow_records/', views.BorrowRecordListView.as_view(), name='borrow_record_list'),

]
