from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True, db_index=True)
    #Slug Validator ensures that slug only has letters, numbers, underscores and hyphens
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    body = models.TextField()
    published = models.BooleanField(default=True)
    published_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', verbose_name='blog_tags')     #A blog could be associated to many tags.

    class Meta:
        ordering = ['-published_on']
        db_table = 'blog'               #table name for model in database

    def __unicode__(self):
        return u'{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('detail', kwargs= {'slug' : self.slug})

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return u'{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])

class Subscribe(models.Model):
    email = models.EmailField(unique=True, help_text='Email')
    first_name = models.CharField(max_length=25, help_text='First Name')
    active = models.BooleanField(default=False)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'{}'.format(self.email)
