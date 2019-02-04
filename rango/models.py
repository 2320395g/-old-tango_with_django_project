from django.db import models

class Category(models.Model):
    name = models.Charfield(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Page(models.model):
    category = models.ForeignKey(Category)
    title = models.CharFiels(max_length=120)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self title
    
