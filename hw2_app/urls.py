from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients_get/', views.clients_get, name='clients_get'),
    path('goods_get/', views.goods_get, name='goods_get'),
    path('orders_get/', views.orders_get, name='orders_get'),
    path('get_orders_by_period/<int:client_id>/<int:time_for_check>', views.get_orders_by_period,
         name='get_orders_by_period'),
    path('add_good_with_image/', views.add_good_with_image, name='add_good_with_image'),
]
