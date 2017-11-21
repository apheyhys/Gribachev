from django.db import models


class Users(models.Model):
    enabled = models.CharField(max_length=1)
    deleted = models.CharField(max_length=1)
    name = models.CharField(max_length=100, blank=True, default='')
    login = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'mgz_users'
        ordering = ['name']


class Brands(models.Model):
    enabled = models.CharField(max_length=1)
    deleted = models.CharField(max_length=1)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'mgz_brands'
        ordering = ['name']


class ProductCategories(models.Model):
    enabled = models.CharField(max_length=1)
    deleted = models.CharField(max_length=1)
    parent_id = models.ForeignKey('self')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    image = models.FilePathField(null=True, blank=True)

    class Meta:
        db_table = u'mgz_products_categories'
        ordering = ['name']


class Products(models.Model):
    enabled = models.CharField(max_length=1)
    deleted = models.CharField(max_length=1)
    category_id = models.ForeignKey(ProductCategories)
    brands_id = models.ForeignKey(Brands)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    date = models.DateTimeField(null=True, blank=True)
    price = models.CharField(max_length=100, blank=True, default='')
    image = models.FilePathField(null=True, blank=True)

    class Meta:
        db_table = u'mgz_products'
        ordering = ['name']



