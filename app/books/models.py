from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('genres.Genre', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

