from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    alive = models.BooleanField(True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    author = models.ForeignKey( Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title