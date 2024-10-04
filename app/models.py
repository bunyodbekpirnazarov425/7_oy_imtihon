from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.ImageField(upload_to='image/', blank=True, null=True)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.cover_image:
            return self.cover_image.url
        else:
            return "https://answers-afd.microsoft.com/static/images/image-not-found.jpg"
    def __str__(self):
        return self.title

# Comment model
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.book.title}'
