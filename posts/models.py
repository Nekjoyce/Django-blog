from django.db import models
from django.urls import reverse # this reverse is a function that allows us to reference a url by the name of the template

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # always put on_delete=models.CASCADE any time you are using a foreignkey. it means that anytime the user deletes its account, everything connected to the account should also be deleted.
    body = models.TextField()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # the get_absolute_url function will return the reverse funtion that takes in the post detail and a dictionary called kwargs and this dictionary 
        return reverse("post_detail", kwargs={"pk": self.pk})
    # the post_detail here sends the detail of the post to the url link that was provided in the home.html. kwargs={"pk": self.pk} helps to specify the particular detail to send using the primary key(pk)