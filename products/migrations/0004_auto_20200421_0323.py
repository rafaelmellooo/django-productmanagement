# Generated by Django 3.0.5 on 2020-04-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200421_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='users',
            field=models.ManyToManyField(blank=True, to='products.User'),
        ),
    ]
