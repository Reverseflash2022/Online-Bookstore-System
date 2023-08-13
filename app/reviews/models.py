from django.db import models

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.user.username} for {self.book.title}'

