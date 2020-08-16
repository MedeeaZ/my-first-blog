from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    Cs = 'CS'
    Cp = 'CP'
    Ac = 'AC'
    Wt = 'WT'
    Op = 'OP'
    Dg = 'DG'
    CHOICES = [
        (Cs, 'Computer Science'), 
        (Cp, 'Coloured Pencils'),
        (Ac, 'Acrylics'),
        (Wt, 'Watercolours'),
        (Op, 'Oil Paints'),
        (Dg, 'Digital'),

    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    tag = models.CharField(max_length=2, choices=CHOICES, default=Cs)
    picture = models.ImageField(blank = True, null = True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

