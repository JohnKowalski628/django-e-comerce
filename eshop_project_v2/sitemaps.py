from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from eshop.models import Category, Product


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['frontpage', 'about', 'contact']


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.date_added
