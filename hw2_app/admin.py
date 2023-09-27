from django.contrib import admin
from .models import Client, Goods, Order


@admin.action(description='Set quantity to zero')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(product_quantity=0)


class GoodsAdmin(admin.ModelAdmin):
    """Goods list"""
    list_display = (
        'product_name', 'product_description', 'product_price', 'product_quantity', 'date_item_add', 'product_image')
    ordering = ['product_name', '-product_quantity']
    list_filter = ['date_item_add', 'product_price', 'product_quantity']
    search_fields = ['product_description', 'product_name']
    search_help_text = 'Search by description field'
    actions = [reset_quantity]

    """Goods"""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']  # displaying fields
    readonly_fields = ['date_item_add']  # set readonly fields
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['product_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['product_description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['product_price', 'product_quantity'],
            }
        ),
        (
            'Дата поступления товара',
            {
                'description': 'Когда поступил товар',
                'fields': ['date_item_add'],
            }
        ),
    ]


class ClientsAdmin(admin.ModelAdmin):
    """Clients list"""
    list_display = ('name', 'email', 'phone_number', 'address', 'reg_date')
    ordering = ['name', '-reg_date']
    list_filter = ['name', 'phone_number', 'reg_date']
    search_fields = ['name', 'email', 'phone_number']
    search_help_text = 'Search by name or phone'

    """Clients"""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']  # displaying fields
    readonly_fields = ['reg_date']  # set readonly fields
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Контактная информация',
                'fields': ['email', 'phone_number'],
            },
        ),
        (
            'Дата регистрации пользователя',
            {
                'description': 'Когда пользователь зарегистрировался',
                'fields': ['reg_date'],
            }
        ),
    ]


class OrdersAdmin(admin.ModelAdmin):
    """Orders list"""
    list_display = ('client', 'total_price', 'order_date')
    ordering = ['order_date', '-total_price']
    list_filter = ['client', 'total_price', 'order_date']
    search_fields = ['client', 'total_price']
    search_help_text = 'Search by Client or total price'

    """Orders"""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']  # displaying fields
    readonly_fields = ['order_date', 'client']  # set readonly fields
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['wide'],
                'description': 'Когда пользователь зарегистрировался',
                'fields': ['order_date', 'total_price'],
            },
        ),
    ]


admin.site.register(Client, ClientsAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrdersAdmin)
