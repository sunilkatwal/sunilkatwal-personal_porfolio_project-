from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    # def image_tag(self):
    #     if self.image:
    #         return mark_safe('<img src="%s" stype=width:45px; height:45px" />' %self.image.url)
    #     else:
    #         return 'No Image found'

    def __str__(self):
        return self.title
