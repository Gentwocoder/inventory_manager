
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from inventorymanager.inventory import views

router = DefaultRouter()
router.register(r"category", views.CategoryView, basename="category")
router.register(r"brand", views.BrandView, basename="brand")
router.register(r"product", views.ProductView, basename="product")
router.register(r"stock", views.StockView, basename="stock")
router.register(r"supplier", views.SupplierView, basename="supplier")
router.register(r"Incoming Order", views.IncomingOrderView, basename="incoming-order")
router.register(r"Outgoing Order", views.OutgoingOrderView, basename="outgoing-order")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
]
