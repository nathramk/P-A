from django.conf.urls import url, include
from django.contrib import admin
from . import views, product_view

app_name = 'control'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^products/(?P<filter_by>[a-zA_Z]+)/$', views.productos, name='productos'),
    url(r'^add_category/$', views.add_category, name='category-add'),
    url(r'^(?P<category_id>[0-9]+)/createProduct/$', views.createProduct, name='product_add'),
    url(r'^(?P<category_id>[0-9]+)/delete_product/(?P<product_id>[0-9]+)/$', views.delete_product,
        name='delete_product'),
    url(r'^(?P<category_id>[0-9]+)/deleteCategory/$', views.deleteCategory, name='category-delete'),
]
# urlpatterns = [
#    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#    url(r'category/add/$', views.CategoryCreate.as_view(), name='category-add'),
#    url(r'category/(?P<pk>[0-9]+)/$', views.CategoryUpdate.as_view(), name='categoryUpdate'),
#    url(r'category/(?P<pk>[0-9]+)/delete/$', views.CategoryDelete.as_view(), name='category-delete'),
#    url(r'product/add/$', product_view.CreateView.as_view(), name='product-add')
# ]
