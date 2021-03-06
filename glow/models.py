from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.
class Category (models.Model):
    title = models.CharField(max_length=20)
    image_path = models.ImageField(upload_to = 'pictures/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def search_by_category(cls,search_term):
        category = cls.objects.filter(title__icontains=search_term)
        print(category)
        return category
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    words = HTMLField(max_length=500,default='Tell me something')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

class Routine (models.Model):
    name = models.CharField(max_length=20,blank=True)
    products = HTMLField(max_length=500,default='Products to use')
    description = HTMLField(max_length=500,default='How to use')
    category = models.ForeignKey(Category,on_delete=models.CASCADE) 
    review = models.ForeignKey(Comment,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def search_by_routine(cls,search_term):
        routine = cls.objects.filter(name__icontains=search_term)
        print(routine)
        return routine
    
    def __str__(self):
        return self.name

