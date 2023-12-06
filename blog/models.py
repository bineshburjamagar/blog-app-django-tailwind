from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify 



class Post(models.Model):


    options = (
    ( 'draft', 'Draft'),
    ( 'published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True, blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey( User, on_delete=models.CASCADE,related_name="blog_posts")
    content = models.TextField()
    status =  models.CharField(max_length=10, choices=options, default='draft') 
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-publish',)

    def save(self, *args, **kwargs):
        if self.slug is None :
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title