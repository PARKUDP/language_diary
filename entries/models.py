from django.db import models
from django.contrib.auth import get_user_model

class Entry(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        null=False, 
        blank=True
        )
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
