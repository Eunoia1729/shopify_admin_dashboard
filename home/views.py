from django.shortcuts import render
import shopify
from shopify_app.decorators import shop_login_required

@shop_login_required
def index(request):
    products = shopify.Product.find()
    orders = shopify.Order.find(order="created_at DESC")
    return render(request, 'home/index.html', {'products': products, 'orders': orders})
