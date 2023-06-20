from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=221)
    email = models.EmailField()
    subject = models.CharField(max_length=221)
    message = models.TextField()
