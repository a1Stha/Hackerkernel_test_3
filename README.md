first I setup the ENVIRONMENT in the django.
then i focoused to work on the first models
here i created a models like  
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    user_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.user_name} - {self.book.title}"


After that i work on the forms ... which helps to create a automatically manners of form without using the html page or not to be apply lots of afforts
After that I worked on the views.py page .... here I created a funtion related to all requirements and then further worked on the app/urls.py


project/urls.py setup previously
