from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'patronymic', 'email', 'city', 'address', 'postal_code', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']

    inlines = [OrderItemAdmin]