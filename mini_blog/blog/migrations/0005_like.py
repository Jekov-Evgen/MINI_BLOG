# Generated by Django 5.0.7 on 2024-08-23 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comments_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP-adress')),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog_user', verbose_name='Публикация')),
            ],
        ),
    ]
