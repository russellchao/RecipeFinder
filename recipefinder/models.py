from django.db import models


class Category(models.Model):
    category_text = models.CharField(max_length=15)

    def __str__(self):
        return self.category_text
    

class Choice(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=30)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
