from django.db import models
from PIL import Image

yes_or_no = (('y','yes'),('n','no'))

class Users(models.Model):
    enabled = models.CharField(max_length=1, choices=yes_or_no, default='y')
    deleted = models.CharField(max_length=1, choices=yes_or_no, default='n')
    name = models.CharField(max_length=100, blank=True, default='')
    login = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = u'mgz_users'
        ordering = ['name']

    def __str__(self):
        return self.name


class Brands(models.Model):
    enabled = models.CharField(max_length=1, choices=yes_or_no, default='y')
    deleted = models.CharField(max_length=1, choices=yes_or_no, default='n')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = u'mgz_brands'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductCategories(models.Model):
    enabled = models.CharField(max_length=1, choices=yes_or_no, default='y')
    deleted = models.CharField(max_length=1, choices=yes_or_no, default='n')
    parent_id = models.ForeignKey('self', null=True, blank=True, default=0)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='img', null=True, blank=True)

    class Meta:
        db_table = u'mgz_products_categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(ProductCategories, self).save(*args, **kwargs)
        sep = '.'
        img = Image.open(self.image.path)
        name = img.filename.split(sep)
        name[1] = 'jpg'
        name = sep.join(name)
        img.save(name)

        name = str(self.image).split(sep)
        name[1] = 'jpg'
        self.image = sep.join(name)
        super(ProductCategories, self).save(*args, **kwargs)


class Products(models.Model):
    enabled = models.CharField(max_length=1, choices=yes_or_no, default='y')
    deleted = models.CharField(max_length=1, choices=yes_or_no, default='n')
    category_id = models.ForeignKey(ProductCategories)
    brands_id = models.ForeignKey(Brands)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    date = models.DateTimeField(null=True, blank=True)
    price = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='img', null=True, blank=True)

    class Meta:
        db_table = u'mgz_products'
        ordering = ['name']

    def __str__(self):
        return self.name


class Colors(models.Model):
    enabled = models.CharField(max_length=1, choices=yes_or_no, default='y')
    deleted = models.CharField(max_length=1, choices=yes_or_no, default='n')
    name = models.CharField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='img', null=True, blank=True)
    products = models.ManyToManyField(Products, through='Samecolor')

    class Meta:
        db_table = u'mgz_colors'
        ordering = ['name']

    def __str__(self):
        return self.name


class Samecolor(models.Model):
    product = models.ForeignKey(Products)
    color = models.ForeignKey(Colors)
    t = models.CharField(max_length=4)

    class Meta:
        db_table = u'mgz_samecolor'
        ordering = ['t']


class Orders(models.Model):
    product_id = models.IntegerField()
    name_product = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    addres = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)
    allow_spam = models.IntegerField()
    order_hash = models.CharField(max_length=50)

    class Meta:
        db_table = u'mgz_orders'
        ordering = ['date']

    def __str__(self):
        return self.customer_name





