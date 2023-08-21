import random

from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category, ProductReview
from cart.cart import Cart


# Create your views here.
def frontpage(request):
    products = Product.objects.filter(is_featured=True, parent=None)
    featured_categories = Category.objects.filter(is_featured=True)
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:4]

    context = {
        'products': products,
        'featured_categories': featured_categories,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products
    }
    return render(request, 'frontpage.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    product.num_visits = product.num_visits + 1
    product.last_visit = datetime.now()
    product.save()

    # Add review
    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)

        return redirect('product_detail', category_slug=category_slug, slug=slug)

    related_products = list(product.category.products.filter(parent=None).exclude(id=product.id))

    if len(related_products) >= 3:
        related_products = random.sample(related_products, 3)

    if product.parent:
        return redirect('product_detail', category_slug=category_slug, slug=product.parent.slug)

    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," % (product.thumbnail.url, product.image.url)

    for image in product.images.all():
        imagesstring = imagesstring + ("{'thumbnail': '%s', 'image': '%s'}," % (image.thumbnail.url, image.image.url))

    context = {
        'product': product,
        'imagesstring': imagesstring,
        'related_products': related_products
    }
    return render(request, 'product_detail.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_added')
    products = category.products.filter(parent=None).filter(price__gte=price_from).filter(price__lte=price_to)

    context = {
        'category': category,
        'products': products.order_by(sorting),
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting
    }

    return render(request, 'category_detail.html', context)


def search(request):
    query = request.GET.get('query')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'products': products,

    }

    return render(request, 'search.html', context)


"""
def search(request):
    query = request.GET.get('query')
    instock = request.GET.get('instock')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_added')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(
        price__gte=price_from).filter(price__lte=price_to)

    if instock:
        products = products.filter(num_available__gte=1)

    context = {
        'query': query,
        'products': products.order_by(sorting),
        'instock': instock,
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting
    }

    return render(request, 'search.html', context)


"""

"""
def sort(request):
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_added')
    products = Product.objects.filter(price__gte=price_from).filter(price__lte=price_to)

    context = {
        'products': products.order_by(sorting),
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting
    }

    return render(request, 'category_detail.html', context)
    
    """

