from django.db import models

# Create your models here.
def Author(models.Model):
    name = models.CharField(max)


def Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)(max_length=100)

def Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

def Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
