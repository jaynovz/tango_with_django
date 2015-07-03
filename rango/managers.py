__author__ = 'bmitchem'
from django.db import models

class JssorMediaManager(models.Manager):
    def assemble_jssor_media(self, num=10):
        media_list = self.order_by('uploaded')[:10]
        return media_list