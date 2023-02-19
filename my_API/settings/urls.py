from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework.routers import DefaultRouter

from cars.views import CarView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('cars', CarView)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
urlpatterns += [
    path('api/v1/', include(router.urls))
]