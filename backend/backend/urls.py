from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/', include('users.urls'))
]

urlpatterns = [
    #path('sentry-debug/', trigger_error),
]