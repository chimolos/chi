from django.contrib import admin
from .models import ShopCart, OrderProduct, Order

# Register your models here.
class ShopCartAdmin(admin.ModelAdmin):
    list_display=('product','user','quantity','price','discount_price','amount','order_placed')
    list_filter=['user']
    list_display_links=['product']

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields=('user','product','price','quantity','amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone','city','total','status','order_placed']
    list_filter=['status']
    readonly_fields=('user','address','city','country','phone','first_name','last_name','ip','city','total')
    can_delete= False
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'price', 'quantity', 'amount']
    list_filter = ['user']


admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)