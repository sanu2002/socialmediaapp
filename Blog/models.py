from django.db import models

# Create your models here.
from django.contrib.auth.models import User






class Blogpost(models.Model):
    title=models.CharField(max_length=1000)
    content=models.CharField(max_length=400)
    image=models.ImageField(upload_to="Blog/images",default="")
    likes=models.ManyToManyField(User,related_name="blog_post")




    def __str__(self):
        return self.title



class Comment(models.Model):
    post=models.ForeignKey(Blogpost,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=350)
    content=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.name




