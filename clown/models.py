from django.contrib.auth.models import User
from django.db import models

class comment(models.Model):
    user = models.ForeignKey(User, on_delete=None, blank=False, default=None)
    text = models.TextField(max_length=1024, blank = True, null = True, default = None)

    def save(self, *args, **kwargs):
        self.user = args[0]
        self.text = args[1]
        super(comment, self).save(*args, **kwargs)
