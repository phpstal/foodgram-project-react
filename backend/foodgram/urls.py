from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('api/', include('recipes.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns