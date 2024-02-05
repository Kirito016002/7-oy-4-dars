from django.http import HttpResponse
from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


# Category
def list_category(request):
    categorys = models.Category.objects.all()
    return render(request, 'category/list.html', {'categorys':categorys})


def create_category(request):
    if request.method == "POST":
        models.Category.objects.create(
            name = request.POST['name']
        )
        return redirect('dashboard:list_category')
    return render(request, 'category/create.html')


def detail_category(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == "POST":
        category.name = request.POST['name']
        category.save()
        return redirect('dashboard:list_category')
    return render(request, 'category/detail.html', {'category':category})


def delete_category(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('dashboard:list_category')


# Product

def product_create(request):
    categorys = models.Category.objects.all()
    context = {
        'categorys':categorys
    }
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        quantity = request.POST['quantity']
        price = request.POST['price']
        currency = request.POST['currency']
        baner_image = request.FILES['baner_image']
        category_id = request.POST['category_id']
        images = request.FILES.getlist('images')
        product = models.Product.objects.create(
            name=name,
            description = description,
            quantity=quantity,
            price=price,
            currency=currency,
            baner_image=baner_image,
            category_id=category_id
        )
        for image in images:
            models.ProductImage.objects.create(
                image=image,
                product=product
            )
        return redirect('dashboard:dashboard')
    return render(request, 'product/create.html', context)


# Auth


def sign_up(request):
    if request.method == "POST":
        User.objects.create_user(username=request.POST['username'],  
                                 password=request.POST['password'],
                                 is_staff=True,
                                 )
        return redirect('dashboard:dashboard')        
    return render(request, 'authentication/sign_up.html')



def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return HttpResponse('Welcome!!!')
            elif user.is_staff:
                return redirect('dashboard:dashboard')
        else:
            return HttpResponse("Username yoki paroldahatolik")
        
    return render(request, 'authentication/sign_in.html')


def sign_out(request):
    logout(request)
    return redirect('main:index')

@login_required
def user_update(request):
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        
        if old_password != new_password:
            user = request.user        
            if user.check_password(old_password):
                user.username = request.POST['username']
                user.set_password(new_password)
                user.save()                                
                update_session_auth_hash(request, user)     
                return redirect('dashboard:dashboard')       
        else:
            return HttpResponse("Parol o`zgarmagan")
        
    return render(request, 'authentication/update.html')