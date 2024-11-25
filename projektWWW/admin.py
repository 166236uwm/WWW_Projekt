from django.contrib import admin
from .models import Users, Product, Recipe, RecipeProduct, Transaction, Delivery, DeliveryProduct

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'role', 'created_at')
    search_fields = ('username', 'name')
    list_filter = ('role',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('productName', 'pricePerUnit')
    search_fields = ('productName',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipeName', 'quantity')
    search_fields = ('recipeName',)

class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'product', 'quantity')
    search_fields = ('recipe__recipeName', 'product__productName')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('POS', 'total_prize', 'created_at')
    search_fields = ('POS__username',)
    list_filter = ('created_at',)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'total_prize', 'deliveryDate')
    search_fields = ('recipient__username', 'product__productName')
    list_filter = ('deliveryDate',)

class DeliveryProductAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'product', 'quantity')
    search_fields = ('recipient__username', 'product__productName')
    list_filter = ('product__productName',)

admin.site.register(Users, UsersAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeProduct, RecipeProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryProduct, DeliveryProductAdmin)