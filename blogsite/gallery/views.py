from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_list(request):
    products=Product.objects.all()
    return render(request,'myapp/index.html',{'products':products})

def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,"myapp/index2.html",{'product':product})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/edit.html', {'form': form})

def delete_product(request,pk):
    product=get_objects_or_404(Product,pk=pk)
    if request.method=='POST':
        product.delete()
        return render(request,'myapp/delete.html',{'product':product})
