from django.db import models


# Create your models here.

class CMProductType(models.Model):
    product_type = models.CharField(max_length=100, verbose_name="product type")

    class Meta:
        verbose_name = "Coffee Machine product type"
        verbose_name_plural = "Coffee Machine product types"

    def __str__(self):
        return self.product_type


class CoffeeMachines(models.Model):
    product_type = models.ForeignKey(CMProductType, null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="cm_type")
    water_line_compatible = models.BooleanField(default=False, verbose_name="water_line_compatible")
    sku = models.CharField(max_length=7)

    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = "Coffee Machine"
        verbose_name_plural = "Coffee Machines"


class CPProductType(models.Model):
    type = models.CharField(max_length=100, verbose_name="product type")

    class Meta:
        verbose_name = "Coffee Pot product type"
        verbose_name_plural = "Coffee Pot product types"

    def __str__(self):
        return self.type


class CoffeeFlavor(models.Model):
    flavor = models.CharField(max_length=100, verbose_name="coffee flavor")

    class Meta:
        verbose_name = "Coffee Flavor"
        verbose_name_plural = "Coffee Flavors"

    def __str__(self):
        return self.flavor


class PackSize(models.Model):
    size = models.CharField(max_length=20, verbose_name="pack size")

    class Meta:
        verbose_name = "Pack Size"
        verbose_name_plural = "Pack Size"

    def __str__(self):
        return self.size


class CoffeePot(models.Model):
    product_type = models.ForeignKey(CPProductType, null=True, blank=True,
                                     on_delete=models.SET_NULL, related_name="cp_type")
    coffee_flavor = models.ForeignKey(CoffeeFlavor, null=True, blank=True,
                                      on_delete=models.SET_NULL, related_name="coffee_flavor")
    pack_size = models.ForeignKey(PackSize, null=True, blank=True,
                                  on_delete=models.SET_NULL, related_name="pack_size")

    sku = models.CharField(max_length=7)

    def __str__(self):
        return self.sku

    class Meta:
        verbose_name = "coffee Pot"
        verbose_name_plural = "coffee Pots"
