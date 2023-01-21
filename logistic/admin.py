from django.contrib import admin

from logistic.models import Product, Stock


@admin.register(Product)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(Stock)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
