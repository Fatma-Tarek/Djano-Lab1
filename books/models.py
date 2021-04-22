from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Isbn(models.Model):
    book_author = models.CharField(max_length=100, null=True)
    isbn_num = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        #return self.isbn_num
        return f"auther {self.book_author} | num {self.isbn_num} "



# Create your models here.
class Book(models.Model):
    #title = models.CharField(max_length =255, null=True , blank=True)
    title = models.CharField(max_length =255)
    content = models.TextField(max_length =2048)
    author = models.ForeignKey(User,  null=True, blank=True,on_delete=models.CASCADE, related_name="books")
    Categories = models.ManyToManyField(Category,null=True, blank=True)
    isbn = models.OneToOneField(Isbn, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ForeignKey(Tag , null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


