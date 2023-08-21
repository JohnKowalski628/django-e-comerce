"""
URL configuration for eshop_project_v2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views

from eshop.views import frontpage, search, contact, about, product_detail, category_detail
from eshop.api import create_checkout_session, api_add_to_cart, api_remove_from_cart, api_checkout
from cart.views import cart_detail, success
from cart.webhook import webhook
from order.views import admin_order_pdf
from coupon.api import api_can_use
from newsletter.api import api_add_subscriber
from userprofile.views import signup, myaccount, become_vendor

from .sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap

sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}

urlpatterns = [

                  path('', frontpage, name='frontpage'),
                  path('search/', search, name='search'),
                  path('cart/', cart_detail, name='cart'),
                  path('hooks/', webhook, name='webhook'),
                  path('cart/success/', success, name='success'),
                  path('contact/', contact, name='contact'),
                  path('about/', about, name='about'),
                  path('admin/', admin.site.urls),
                  path('admin/admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),

                  # Auth

                  path('myaccount/', myaccount, name='myaccount'),
                  path('signup/', signup, name='signup'),
                  path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', views.LogoutView.as_view(), name='logout'),

                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

                  path('api/can_use/', api_can_use, name='api_can_use'),
                  path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
                  # path('api/validate_payment/', validate_payment, name='validate_payment'),
                  path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
                  path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
                  path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),

                  # Vendor
                  path('become-vendor/', become_vendor, name='become_vendor'),

                  # Store

                  path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
                  path('<slug:slug>/', category_detail, name='category_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
