from django.db import models
from products.models import ProductsModel
from accounts.models import UserModel

class OrderingModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete = models.CASCADE,
                                null = False, blank = False, related_name = 'orders')
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE,
                                    null = False, blank = False, related_name = 'orders')
    number = models.IntegerField(blank = False, null = False)
    description = models.TextField(blank = True, null = True)
    checked = models.BooleanField(default = False)
