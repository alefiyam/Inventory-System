from django.contrib import admin
from inventory.models import Item, Category, Vendor

for model in (Category, Item, Vendor):
    admin.site.register(model)
