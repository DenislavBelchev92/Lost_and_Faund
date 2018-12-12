from django.db import models

class Post(models.Model):
    owner = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1250)  
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.owner + ' - ' + self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.CharField(max_length=250)
    content = models.TextField(max_length=1250)  
