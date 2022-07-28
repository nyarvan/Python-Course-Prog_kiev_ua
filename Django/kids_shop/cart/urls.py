from django.urls import path

from .views import cart_detail, cart_add, cart_remove, cart_push

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add_buy/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name="cart_remove"),
    path('add/<int:product_id>/', cart_push, name="cart_push"),
]