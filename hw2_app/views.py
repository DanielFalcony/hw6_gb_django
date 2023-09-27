from datetime import datetime, timedelta

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging

from hw2_app.forms import GoodAddForm
from hw2_app.management.commands.fake_date import generate_random_date
from hw2_app.models import Client, Goods, Order

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('Hello page')


def clients_get(request):
    logger.info('Customers list has been requested.')
    result = '<br>'.join(str(i) for i in Client.objects.all())
    return HttpResponse(result)


def goods_get(request):
    logger.info('Goods list has been requested.')
    result = '<br>'.join(str(i) for i in Goods.objects.all())
    return HttpResponse(result)


def orders_get(request):
    logger.info('Order list has been requested.')
    result = '<br>'.join(str(i) for i in Order.objects.all())
    return HttpResponse(result)


def get_orders_by_period(request, client_id, time_for_check):
    client = get_object_or_404(Client, pk=client_id)
    time_ago = datetime.now() - timedelta(days=time_for_check)
    orders = Order.objects.filter(client=client, order_date__gte=time_ago).order_by('-order_date')
    if orders.exists():
        products = Goods.objects.filter(order__in=orders).distinct()
        return render(request, 'hw2_app/get_orders_by_period.html',
                      {'client': client, 'result': products, 'time': time_for_check})
    else:
        return render(request, 'hw2_app/get_orders_by_period.html',
                      {'client': client, 'result': 'Нет заказов!', 'time': time_for_check})


def add_good_with_image(request):
    if request.method == 'POST':
        form = GoodAddForm(request.POST, request.FILES)
        message = 'Данные добавлены!'
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_description = form.cleaned_data['product_description']
            product_price = form.cleaned_data['product_price']
            product_quantity = form.cleaned_data['product_quantity']
            product_image = form.cleaned_data['product_image']
            fs = FileSystemStorage()
            fs.save(product_image.name, product_image)
            logger.info(
                f'Добавлен товар: {product_name=}, {product_description=}, {product_price=}, {product_quantity=}, '
                f'{product_image.name}.')
            good = Goods(product_name=product_name, product_description=product_description,
                         product_price=product_price, product_quantity=product_quantity,
                         product_image=product_image, date_item_add=generate_random_date(2021, 2023))
            good.save()
    else:
        form = GoodAddForm()
        message = 'Заполните форму'
    return render(request, 'hw2_app/add_good_with_image.html', {'form': form, 'message': message})
