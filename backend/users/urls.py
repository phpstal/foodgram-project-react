from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (FoodUserViewSet, GetToken,
                    GetConfirmationCode)


router = DefaultRouter()
router.register('users', FoodUserViewSet, basename='users')


auth_urls = [
    path('token/', GetToken.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('email/', GetConfirmationCode.as_view(), name='confirmation_code')
]

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('', include(router.urls)),
]
