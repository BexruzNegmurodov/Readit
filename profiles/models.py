from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=201, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def name(self):
        full_name = []
        if self.user.first_name:
            full_name.append(self.user.first_name)
        if self.user.last_name:
            full_name.append(self.user.last_name)
        name = ' '.join(full_name)
        if name:
            return name
        return self.user.username


def user_post_save(instance, sender, created, *args, **kwargs):
    if created:
        obj = Profile.objects.create(user=instance)
        obj.save()
        return obj
    return None


post_save.connect(user_post_save, sender=User)
