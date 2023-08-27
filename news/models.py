from django.db import models

# Create your models here.


class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = "News"
