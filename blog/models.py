from django.db import models
from accounts.models import Account
from tinymce import HTMLField
from django.utils.translation import gettext_lazy as _ # this will use to translate text to other languages






class Author(models.Model):
    user            = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True,blank=True,upload_to='author') 

    def __str__(self):
        return self.user.first_name +" "+ self.user.last_name
    


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user        = models.ForeignKey(Account,on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)


    def __str__(self):
        return self.user.first_name + " "+self.user.last_name 


class Post(models.Model):
    title     = models.CharField(max_length=100)
    overview  = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    content   = HTMLField()
    author    = models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True,upload_to='post',null=True)
    featured  = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')
    

