from django.db import models
from profiles.models import Profile


class Feedback(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        full_name = []
        if self.author.user.first_name:
            full_name.append(self.author.user.first_name)
        if self.author.user.last_name:
            full_name.append(self.author.user.last_name)
        name = ' '.join(full_name)
        if name:
            return name
        return self.author.user.username
