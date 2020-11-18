from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    vin = models.CharField(verbose_name='Вин', max_length=64, unique=True, db_index=True)
    color = models.CharField(verbose_name='Цвет', max_length=64)
    brand = models.CharField(verbose_name='Бренд', max_length=64)
    CAR_TYPES = (
        (1, 'Хечбек'),
        (2, 'Седан'),
        (3, 'Купе'),
        (4, 'Универсал')
    )
    car_type = models.IntegerField(verbose_name='Тип', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'