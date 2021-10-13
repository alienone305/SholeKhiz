from django.db import models

class ProductsModel(models.Model):
    name = models.CharField(max_length = 264, blank = False, null = False)
    picture = models.ImageField(blank = False, null = False,default = r'products/default/default.jpeg',
                                upload_to=r'products/')
    description = models.TextField(default='',null = True, blank = True)
    is_towerdryer = models.BooleanField()
    is_radiator = models.BooleanField()
    is_waterheater = models.BooleanField()
    is_package = models.BooleanField()
    cataloge = models.FileField(blank = False, null = False, default = r'cataloges/default/default.jpeg',
                                upload_to=r'cataloges/')

    def save(self, *args, **kwargs):
        try:
            format = self.picture.name.lower()
            if format.endswith('.jpg') or format.endswith('.png') or format.endswith('.jpeg'):
                pass
            else:
                self.picture = None
        except:
            pass
        super(ProductsModel, self).save(*args, **kwargs)
