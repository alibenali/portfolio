from django.db import models
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = RichTextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
