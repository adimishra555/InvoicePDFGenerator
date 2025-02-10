from django.urls import path
from .views import generate_invoice, get_all_orders, get_order_details, invoice_template

urlpatterns = [
    path("invoice/<str:order_id>/", generate_invoice, name="generate_invoice"),
    path("orders/", get_all_orders, name="get_all_orders"),  
    path("orders/<str:order_id>/", get_order_details, name="get_order_details"),
    path("invoice-template/<str:order_id>/", invoice_template, name="invoice_template"),  
]