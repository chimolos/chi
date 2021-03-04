from django.db import models
from django.contrib.auth.models import User

from django.forms import ModelForm
from product.models import Product

# Create your models here.
class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    quantity = models.IntegerField(blank=True, null=True, editable=False)
    order_placed = models.BooleanField(default=False, editable=False)
    order_code = models.CharField(max_length=70, editable=False,default='40gHyTui')

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        if self.product_id is not None:
            return (self.product.price)

    @property
    def discount_price(self):
        if self.product_id is not None:
            return (self.product.discount_price)

    @property
    def amount(self):
        if self.product_id is None:
            return (None)
        else:
            if self.product.discount_price:
                return (self.product.discount_price * self.quantity)
            else:
                return(self.product.price * self.quantity)

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = []
        # widgets = {
        #     '':SelectMultiple(attrs={'type':'text', 'id': 'myInput', 'placeholder':'Size...', 'maxlength':'10', 'size':'10'}),
        #     '':SelectMultiple(attrs={'type':'text', 'id': 'myInput', 'placeholder':'Size...', 'maxlength':'10', 'size':'10'})
        # }

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total = models.FloatField(null=True, blank=True)
    order_placed = models.BooleanField(default=False, editable=False)
    order_code = models.CharField(max_length=70, editable=False,default='40gHyTui')
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    total = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name','address','phone','city','country']

class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_placed = models.BooleanField(default=False, editable=False)
    order_code = models.CharField(max_length=70, editable=False,default='40gHyTui')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title