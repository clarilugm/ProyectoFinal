# Generated by Django 4.1.3 on 2023-01-09 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_alter_blog_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(upload_to='AppBlog/'),
        ),
    ]