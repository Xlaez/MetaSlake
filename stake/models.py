from uuid import uuid4

from autoslug import AutoSlugField
from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.


class Chain(models.Model):
    id = models.UUIDField(default=uuid4(), editable=False, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', always_update=True, null=True)
    symbol = models.CharField(max_length=255, null=True)
    logo = models.ImageField(default='no-image.png', null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.name)


class Stake(models.Model):
    id = models.UUIDField(default=uuid4(), editable=False, primary_key=True)
    asset_to_stake = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='asset_to_stake', always_update=True)
    asset_image = models.ImageField(default='no-image.png', null=True)
    asset_to_win = models.CharField(max_length=255, null=True)
    apy = models.DecimalField(max_digits=6, decimal_places=2, null=True, validators=[MinValueValidator(0)])
    contract_address = models.CharField(max_length=1000, null=True)
    chain = models.ForeignKey(Chain, on_delete=models.DO_NOTHING, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.asset_to_stake)
