# Generated by Django 4.1.3 on 2023-01-02 17:47

import ckeditor.fields
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
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateField()),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(upload_to='blog/')),
                ('usuarioFK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='avatar/')),
                ('usuarioFK', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]