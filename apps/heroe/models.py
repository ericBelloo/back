from django.db import models
from mixins.models import BaseModel


class Editorial(BaseModel):

    class Meta:
        ordering = ['name']


class Heroes(BaseModel):
    description = models.CharField(max_length=100, null=False, blank=False)
    apparition = models.DateField()
    image = models.ImageField(upload_to='media/heroes', null=True)
    # Foreign Key
    editorial = models.ForeignKey(Editorial, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']
