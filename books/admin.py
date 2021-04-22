from django.contrib import admin
from .models import Book , Category, Isbn , Tag
from .forms import BookForm


class BookInLine(admin.StackedInline):
    model = Book
    max_num = 3
    extra = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [BookInLine]


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ("title", "author", "content")
    list_filter = ("Categories",)
    search_fields = ("title",)

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn)
admin.site.register(Tag ,TagAdmin)