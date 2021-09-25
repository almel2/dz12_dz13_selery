from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    birthday = models.CharField(max_length=150)
    birth_loc = models.CharField(max_length=150)
    about = models.TextField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote


from django.db import models

# Create your models here.
