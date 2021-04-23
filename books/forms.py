from django import forms
from .models import Book
from .models import Category
from django.core.exceptions import ValidationError


class BookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("isbn",)

        #def clean_title(self):
        #    title = self.cleaned_data.get("title")
        #    if (len(title) < 10) or (len(title) > 50):
        #        raise ValidationError("book title must be  between 10 & 50 characters")
        #   return title

        #def clean_category (self):
        #    category = self.cleaned_data.get("Categories")
        #    if min(category, key = len ) < 2:
         #       raise ValidationError("The minimum length of a category name is 2 characters")
         #   return category 
        
    def clean(self):
        super(BookForm , self).clean()
        title = self.cleaned_data.get('title')
        category = self.cleaned_data.get("Categories")
        #nameOfCategory = Category.objects.filter(id=category).first()
        #category = self.cleaned_data.get("Categories")
        #newName = nameOfCategory[0].title
        #print(nameOfCategory )
        ##############################
        #newName = Category.objects.order_by('id', category).first()
        # Category.objects.filter(category=category, subcategory=subcategory, kind=kind[0], available=True)

        if (len(title) < 10) or (len(title) > 50):
            raise ValidationError("book title must be  between 10 & 50 characters")
        #if len(nameOfCategory) < 2:
        #   raise ValidationError("The minimum length of a category name is 2 characters")

        return self.cleaned_data

