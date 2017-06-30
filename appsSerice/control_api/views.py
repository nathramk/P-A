from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from appsSerice.control.models.categoria import Category
from appsSerice.control.models.producto import Product
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, CategoryForm, UserForm
from django.db.models import Q

IMAGE_TYPE = ['png', 'jpg', 'jpeg']


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'control/login.html')
    else:
        categories = Category.objects.filter(user=request.user)
        products_results = Product.objects.all()
        query = request.GET.get("q")
        if query:
            categories = categories.filter(
                Q(name_category__icontains=query)
            ).distinct()
            products_results = products_results.filter(
                Q(cod_product__icontains=query) |
                Q(nome_product__icontains=query)
            ).distinct()
            return render(request, 'control/index.html', {
                'categories': categories,
                'productos': products_results,
            })
        else:
            return render(request, 'control/index.html', {'categories': categories})


def detail(request, category_id):
    if not request.user.is_authenticated():
        return render(request, 'control/login.html')
    else:
        user = request.user
        category = get_object_or_404(Category, pk=category_id)
        return render(request, 'control/detail.html', {'category': category, 'user': user})


def add_category(request):
    if not request.user.is_authenticated():
        return render(request, 'control/login.html')
    else:
        modelform = CategoryForm(request.POST or None, request.FILES or None)
        if modelform.is_valid():
            category = modelform.save(commit=False)
            category.category_logo = request.FILES['category_logo']
            file_type = category.category_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_TYPE:
                context = {
                    'category': category,
                    'form': modelform,
                    'error_message': 'nesitas los archivos con extencion .jpg .png o .jpeg'
                }
                return render(request, 'control/category_form.html', context)
            category.save()
            return render(request, 'control/detail.html', {'category': category})
        context = {
            "form": modelform
        }
        return render(request, 'control/category_form.html', context)


def deleteCategory(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    categories = Category.objects.filter(user=request.user)
    return render(request, 'control/index.html', {'categories': categories})


#    categories = get_object_or_404(Category, pk=category_id)
#    if request.method == 'POST':
#        categories.delete()
#        return redirect('/api/control/')
#    return render(request, 'control/index.html', {'categories': categories})


def createProduct(request, category_id):
    modelForm = ProductForm(request.POST or None, request.FILES or None)
    category = get_object_or_404(Category, pk=category_id)
    if modelForm.is_valid():
        category_products = category.product_set.all()
        for k in category_products:
            if k.cod_product == modelForm.cleaned_data.get("cod_product"):
                context = {
                    'category': category,
                    'form': modelForm,
                    'error_message': 'ya ahs añadido es preducto'
                }
                return render(request, 'control/product_form.html', context)
        product = modelForm.save(commit=False)
        product.category = category
        product.product_logo = request.FILES['product_logo']
        file_type = product.product_logo.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_TYPE:
            context = {
                'category': category,
                'form': modelForm,
                'error_message': 'nesitas los archivos con extencion .jpg .png o .jpeg'
            }
            return render(request, 'control/product_form.html', context)
        product.save()
        return render(request, 'control/detail.html', {'category': category})
    context = {
        'category': category,
        'form': modelForm
    }
    return render(request, 'control/product_form.html', context)


def singleProduct_view(request, category_id, product_id):
    category = get_object_or_404(Category, pk=category_id)
    product = Product.objects.get(pk=product_id)

    context = {
        'category': category,
        'product': product,
    }
    return render(request, 'control/singleProduct.html', context)


def delete_product(request, category_id, product_id):
    category = get_object_or_404(Category, pk=category_id)
    product = Product.objects.get(pk=product_id)
    product.delete()
    return render(request, 'control/detail.html', {'category': category})


def productos(request, filter_by):
    if not request.user.is_authenticated():
        return request(request, 'control/login.html')
    else:
        try:
            product_ids = []
            for category in Category.objects.filter(user=request.user):
                for product in category.product_set.all():
                    product_ids.append(product.pk)
            user_product = Product.objects.filter(pk__in=product_ids)
        except Category.DoesNotExist:
            user_product = user_product
        context = {
            'user_product': user_product,
            'filter_by': filter_by
        }
        return render(request, 'control/productos.html', context)


def register(request):
    modelForm = UserForm(request.POST or None)
    if modelForm.is_valid():
        user = modelForm.save(commit=False)
        username = modelForm.cleaned_data['username']
        password = modelForm.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                categories = Category.objects.filter(user=request.user)
                return render(request, 'control/index.html', {'categories': categories})
    context = {
        'form': modelForm
    }
    return render(request, 'control/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                categories = Category.objects.filter(user=request.user)
                return render(request, 'control/index.html', {'categories': categories})
            else:
                return render(request, 'control/login.html', {'error_message': 'invalid login'})
        else:
            return render(request, 'control/login.html', {'error_message': 'invalid login'})
    return render(request, 'control/login.html')


# class IndexView(generic.ListView):
#    template_name = 'control/index.html'
#    context_object_name = 'all_categories'

#    def get_queryset(self):
#        return Category.objects.all()


# class DetailView(generic.DetailView):
#    model = Category
#    template_name = 'control/detail.html'


# class CategoryCreate(CreateView):
#    model = Category
#    fields = ['name_category', 'category_logo']


# class CategoryUpdate(UpdateView):
#    model = Category
#    fields = ['name_category', 'category_logo']


# class CategoryDelete(DeleteView):
#   model = Category
#   success_url = reverse_lazy('control:index')
