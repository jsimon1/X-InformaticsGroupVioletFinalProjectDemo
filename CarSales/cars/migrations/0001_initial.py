# Generated by Django 2.0.4 on 2018-04-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_web', models.URLField()),
                ('car_make', models.CharField(max_length=200)),
                ('car_year', models.DateTimeField(verbose_name='Model Year')),
                ('car_model', models.CharField(max_length=200)),
                ('car_image', models.ImageField(upload_to='cars')),
                ('car_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dealer_name', models.CharField(max_length=200)),
                ('dealer_web', models.URLField()),
                ('dealer_zip', models.IntegerField(default=0)),
            ],
        ),
    ]
