from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Reviews(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    clap = models.IntegerField(blank=True, default=0)
