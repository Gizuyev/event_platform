from django.db import models
from app.users.models import CustomUser


class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    starts = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=50)
    owner = models.ForeignKey(to=CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.email} on {self.event.title}'
