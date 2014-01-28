from django.db import models

# Create your models here.


class Client(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField(default=0)
    city = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)
    phones = models.IntegerField(default=0)
    fax = models.IntegerField(default=0)
    email = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Pricelist(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField(default=0)


class Promotional(models.Model):
    item_title = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)






