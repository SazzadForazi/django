from django.db import models
from catagory.models import Category
from authors.models import Author

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TimeField()
    Category = models.ManyToManyField(Category)
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    