
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from inventorymanager.inventory import views
from inventorymanager.core.views import RegisterView, CustomTokenView, ProfileView, LogoutView, LoginView, VerifyEmailView

router = DefaultRouter()
router.register(r"category", views.CategoryView, basename="category")
router.register(r"brand", views.BrandView, basename="brand")
router.register(r"product", views.ProductView, basename="product")
router.register(r"stock", views.StockView, basename="stock")
router.register(r"supplier", views.SupplierView, basename="supplier")
router.register(r"Incoming Order", views.IncomingOrderView, basename="incoming-order")
router.register(r"Outgoing Order", views.OutgoingOrderView, basename="outgoing-order")
# router.register(r"register", RegisterView, basename="register")
# router.register(r"token", CustomTokenView, basename="token")
# router.register(r"token/refresh", TokenRefreshView.as_view(), basename="token_refresh")
# router.register(r"profile", ProfileView, basename="profile")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/token/", CustomTokenView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/profile/", ProfileView.as_view(), name="profile"),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/verify-email/<uuid:token>/", VerifyEmailView.as_view(), name="verify-email"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
]
