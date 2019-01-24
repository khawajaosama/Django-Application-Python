from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True) # blank=true for it is blank field
# add in author later
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

# models are a class that represent a single table in a data base