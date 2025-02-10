from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrderDB
import datetime

@api_view(["GET"])
def invoice_template(request, order_id):
    try:
        order = get_object_or_404(OrderDB, order_id=order_id)

        context = {
            "order_id": order.order_id,
            "username": order.user.username,
            "email": order.user.email,
            "phone": order.user.phone,
            "address": f"{order.user.address_line1}, {order.user.city}, {order.user.state}, {order.user.country}",
            "product_title": order.product.product_title,
            "brand": order.product.brand,
            "price": float(order.product.price),
            "quantity": order.quantity,
            "total_amount": float(order.total_amount),
            "created_at": order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

        return render(request, "invoice_template.html", context)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
