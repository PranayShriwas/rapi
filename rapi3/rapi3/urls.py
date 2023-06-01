from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from home.ProductViewset import ProductViewset
router = routers.DefaultRouter()
router.register(r'product', ProductViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
