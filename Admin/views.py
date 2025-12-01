from django.shortcuts import render, redirect, get_object_or_404
from django_daraja.mpesa.core import MpesaClient
from .models import Product

# Create your views here.
def admin(request):
    #viewing the products/ populating
    products = Product.objects.all()
    return render(request, 'admin.html', {'products': products})

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        Product.objects.create(
            name=name,
            price=price,
            description=description
        )
        return  redirect('admin')

    return render(request, 'add_item.html')

def delete_item(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('admin')

def update_item(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        
        product.save()
        return redirect('admin')
    
    return render(request, 'update_item.html', {'product':product})

def payment(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        amount = int(request.POST.get('amount'))
        
        client = MpesaClient()
        
        account_ref = 'S. Tech Institute'
        desc = 'support services payment'
        
        callback_url = 'https://callback.com/url'
        
        response = client.stk_push(
            phone_number=phone,
            amount=amount,
            account_reference=account_ref,
            transaction_desc=desc,
            callback_url=callback_url
        )
        return render(request, "payment.html", {"message":"STK Push sent!"})
    return render(request, 'payment.html')
        