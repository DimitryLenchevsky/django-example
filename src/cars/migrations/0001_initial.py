# Generated by Django 3.1.2 on 2020-11-17 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Вин')),
                ('color', models.CharField(max_length=64, verbose_name='Цвет')),
                ('brand', models.CharField(max_length=64, verbose_name='Бренд')),
                ('car_type', models.IntegerField(choices=[(1, 'Хечбек'), (2, 'Седан'), (3, 'Купе'), (4, 'Универсал')], verbose_name='Тип')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
