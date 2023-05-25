# Generated by Django 4.2.1 on 2023-05-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Pengguna',
            },
        ),
    ]
