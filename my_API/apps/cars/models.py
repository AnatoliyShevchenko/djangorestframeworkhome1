from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class MarkCar(models.Model):
    """Make some car mark."""

    mark_title = models.CharField(
        verbose_name='марка автомобиля',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'марка'
        verbose_name_plural = 'марки'

    def __str__(self) -> str:
        return self.mark_title

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        if not self.mark_title:
            raise ValidationError('field must be not empty')
        elif len(self.mark_title) < 3:
            raise ValidationError('Mark title must contain more than 3 symbols')
        return super().clean()


class ModelCar(models.Model):
    """Surprise mf. Here we will create models for cars."""

    model_title = models.CharField(
        verbose_name='модель автомобиля',
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'модель'
        verbose_name_plural = 'модели'

    def __str__(self) -> str:
        return self.model_title

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        if not self.model_title:
            raise ValidationError('field must be not empty')
        elif len(self.model_title) < 5:
            raise ValidationError('Mark title must contain more than 5 symbols')
        return super().clean()


class ColorCar(models.Model):
    """Let's paint car."""

    color_title = models.CharField(
        verbose_name='название цвета',
        max_length=20,
        unique=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'

    def __str__(self) -> str:
        return self.color_title


class Car(models.Model):
    """Custom model Car (for homework 13.02)."""

    mark = models.ForeignKey(
        to=MarkCar,
        on_delete=models.CASCADE
    )
    model = models.ForeignKey(
        to=ModelCar,
        on_delete=models.CASCADE
    )
    color = models.ForeignKey(
        to=ColorCar,
        on_delete=models.CASCADE
    )
    year_of_issue = models.IntegerField(
        verbose_name='год выпуска',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'

    def __str__(self) -> str:
        return f'{self.mark} | {self.model} | \
            {self.color} | {self.year_of_issue}'

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        if self.year_of_issue <= 0:
            raise ValidationError('it is impossible')
        elif self.year_of_issue < 1980:
            raise ValidationError('too old')
        elif not self.year_of_issue:
            raise ValidationError('fields must be not empty')
        return super().clean()