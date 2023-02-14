from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from cars.views import CarView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]