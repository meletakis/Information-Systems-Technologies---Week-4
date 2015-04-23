from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, blank=False )
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=512)

    def __str__(self):             
		return str(self.id)

class Comments(models.Model):
    postId = models.ForeignKey(Posts)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=512)
    email = models.EmailField()

    def __str__(self):             
		return str(self.id)