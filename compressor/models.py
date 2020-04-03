from django.db import models


class Images(models.Model):

    image_format_choices = (
        ('jpg', 'jpg'),
        ('jpeg', 'jpeg'),
        ('png', 'png'),
        ('webp', 'webp')
    )

    id = models.AutoField(primary_key=True)
    original_img = models.ImageField(upload_to='original/', null=True)
    original_size = models.TextField(null=True)
    quality = models.IntegerField(null=True, blank=True)
    converted_img = models.ImageField(upload_to='converted/', null=True)
    converted_size = models.TextField(null=True)
    image_format = models.CharField(
        max_length=5, null=True, choices=image_format_choices, blank=True)
