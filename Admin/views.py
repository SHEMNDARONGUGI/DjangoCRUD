from django.shortcuts import render, redirect, get_object_or_404
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
        