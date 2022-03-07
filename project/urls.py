from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# from shop.views import CategoryView, ProductView
from shop.views import CategoryViewset, ProductViewset, ArticleViewset, AdminCategoryViewset, AdminArticleViewset, AdminProductViewset

router = routers.SimpleRouter()

router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='articlee')
router.register('admin/category', AdminCategoryViewset, basename='admin-category')
router.register('admin/product',AdminProductViewset, basename='admin-product')
router.register('admin/article', AdminArticleViewset, basename='admin-article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/category/', CategoryView.as_view()),
    # path('api/product/', ProductView.as_view()),
    path('api/', include(router.urls)),
]
