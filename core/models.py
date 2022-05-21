from django.db import models
from .utils import generate_delete_link, generate_shorten_link

class Link(models.Model):

    class Meta:
        ordering = ['-created_at']

    origin = models.URLField(max_length=512, null=False, blank=False)
    slug = models.CharField(max_length=16, unique=True, blank=True)
    # delete_slug = models.CharField(max_length=32, unique=True, blank=True)
    is_enabled = models.BooleanField(null=False, default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_shorten_link(self)

        # if not self.delete_slug:
        #     self.delete_slug = generate_delete_link(self)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.origin


class Visitor(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='visitor')
    ip = models.GenericIPAddressField()
    useragent = models.CharField(max_length=128, blank=True)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip