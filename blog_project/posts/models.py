from django.db import models
from catagory.models import Category
from authors.models import Author

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    Category = models.ManyToManyField(Category)
    Author = models.ForeignKey(Author,on_delete=models.CASCADE) #many to one
    
    def __str__(self):
        return self.title
    