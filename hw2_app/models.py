from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    reg_date = models.DateField()

    def __str__(self):
        return f'Client name: {self.name}, ' \
               f'email: {self.email}, ' \
               f'phone: {self.phone_number}, ' \
               f'address: {self.address}, ' \
               f'reg_date: {self.reg_date}'


class Goods(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField()
    date_item_add = models.DateField()
    product_image = models.ImageField()

    def __str__(self):
        return f'product_name: {self.product_name}, ' \
               f'price: {self.product_price}, '


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f'client: {self.client}, ' \
               f'total_price: {self.total_price}, ' \
               f'order_date: {self.order_date}'
