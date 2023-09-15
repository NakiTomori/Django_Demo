from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length= 300)
    content = models.TextField(max_length= 1000)
    image = models.URLField()

    class Meta:
        db_table = "tbBlog"
