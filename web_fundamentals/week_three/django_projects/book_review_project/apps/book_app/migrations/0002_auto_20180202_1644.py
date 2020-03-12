# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-02 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration_app', '0002_auto_20180127_1754'),
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='book_app.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='login_registration_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='book',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='liked_users',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
