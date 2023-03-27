# Generated by Django 4.1.6 on 2023-02-16 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=150, verbose_name='Nombre')),
                ('telefono_movil', models.CharField(blank=True, default='', max_length=9, null=True, verbose_name='Tlfno. móvil')),
                ('telefono_fijo', models.CharField(blank=True, default='+34', max_length=9, null=True, verbose_name='Tlfno. fijo')),
                ('mail', models.EmailField(blank=True, default='', max_length=150, null=True, verbose_name='EMail')),
                ('direccion', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Dirección postal')),
                ('foto', models.FileField(blank=True, max_length=254, null=True, upload_to='', verbose_name='Foto')),
                ('empresa', models.CharField(default='Proyecto A', max_length=150)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'contactos',
            },
        ),
    ]
