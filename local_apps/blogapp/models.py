from django.db import models
from django.template.defaultfilters import slugify

class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.SlugField()
	date_published = models.DateTimeField('date published')
	date_last_modified = models.DateTimeField('date last modified')


	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Entry, self).save(*args, **kwargs)
	