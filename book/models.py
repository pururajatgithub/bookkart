from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    book_type = models.CharField(max_length=100)
    price = models.FloatField()
    available_for = models.CharField(max_length=100, blank=True)
    book_image = models.ImageField(upload_to='book/static/images',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.book_name
    
    def save_book(self):
        self.save()
    
    def delete_book(self):
        self.delete()
    
    def update_book(self):
        self.update()
    
    @classmethod
    def search_book(self,cls,search_term):
        books = cls.objects.filter(book_name__icontains=self.book_name)
        return books

    
