from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    display = models.BooleanField(default=True)
    image1 = models.ImageField(blank=False, default='default.png', upload_to='projects')
    image2 = models.ImageField(blank=True, upload_to='projects')
    image3 = models.ImageField(blank=True, upload_to='projects')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})  # provide string of url

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name='replies', on_delete=models.CASCADE, blank=True)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title,  str(self.user.username))


