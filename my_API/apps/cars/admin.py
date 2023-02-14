from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from typing import Optional

from .models import MarkCar, ModelCar, ColorCar, Car

# Register your models here.
class MarkCarAdmin(admin.ModelAdmin):
    """Admin for mark."""

    model = MarkCar
    list_display = [
        'mark_title'
    ]


class ModelCarAdmin(admin.ModelAdmin):
    """Admin for model."""

    model = ModelCar
    list_display = [
        'model_title'
    ]


class ColorCarAdmin(admin.ModelAdmin):
    """Admin for paint car."""

    model = ColorCar
    list_display = [
        'color_title'
    ]


class CarAdmin(admin.ModelAdmin):
    """Admin for create car."""

    model = Car
    list_display = [
        'mark',
        'model',
        'color',
        'year_of_issue'
    ]


admin.site.register(MarkCar, MarkCarAdmin)
admin.site.register(ModelCar, ModelCarAdmin)
admin.site.register(ColorCar, ColorCarAdmin)
admin.site.register(Car, CarAdmin)