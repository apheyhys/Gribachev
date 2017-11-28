from django.contrib import admin
from magazin.catalog.models import *

class UsersAdmin(admin.ModelAdmin):
    radio_fields = {"enabled": admin.HORIZONTAL, "deleted": admin.HORIZONTAL}
    pass

class ProductCategoriesAdmin(admin.ModelAdmin):
    radio_fields = {"enabled": admin.HORIZONTAL, "deleted": admin.HORIZONTAL}
    pass

class BrandsAdmin(admin.ModelAdmin):
    radio_fields = {"enabled": admin.HORIZONTAL, "deleted": admin.HORIZONTAL}
    pass

class ColorsAdmin(admin.ModelAdmin):
    radio_fields = {"enabled": admin.HORIZONTAL, "deleted": admin.HORIZONTAL}
    pass

class ProductsAdmin(admin.ModelAdmin):
    radio_fields = {"enabled": admin.HORIZONTAL, "deleted": admin.HORIZONTAL}
    pass

class SamecolorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users, UsersAdmin)
admin.site.register(Brands, BrandsAdmin)
admin.site.register(ProductCategories, ProductCategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Colors, ColorsAdmin)
admin.site.register(Samecolor, SamecolorAdmin)