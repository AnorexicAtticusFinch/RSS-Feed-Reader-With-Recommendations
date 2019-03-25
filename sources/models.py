from django.db import models

# Create your models here.

class Source(models.Model):
    link      = models.CharField(max_length = 150,default='https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
    file_name = models.CharField(max_length=50,default='TOP_STORIES')
