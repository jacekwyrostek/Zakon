from django.db import models

# Create your models here.
class News(models.Model):
    pubDate=models.DateField(auto_now_add=True)
    title=models.CharField(max_length=100)
    txt=models.TextField()
    class Meta:
        ordering = ['-pubDate']
