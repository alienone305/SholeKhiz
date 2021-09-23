from django.db import models

class GalleryModel(models.Model):
    picture = models.ImageField(default = r'gallery/default/default.png',
                                 upload_to=r'gallery/')
    description = models.TextField(null = True, blank = True)
                                 
