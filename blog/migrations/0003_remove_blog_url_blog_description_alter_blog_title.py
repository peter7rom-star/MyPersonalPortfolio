# Generated by Django 4.1 on 2022-12-13 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_description_remove_blog_image_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default='Blog description', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]