from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Book, Comment

admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):


    def get_image(self, books):
        if books.image:
            return mark_safe(f'<img src="{books.image.url}" width="100px">')
        else:
            return mark_safe(
                f'<img src="https://answers-afd.microsoft.com/static/images/image-not-found.jpg" width="75px">')
