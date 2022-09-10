# Generated by Django 4.1 on 2022-09-04 08:08

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
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('interests', models.TextField(max_length=500)),
                ('skills', models.TextField(max_length=500)),
                ('profession', models.CharField(max_length=200)),
                ('blocked_user', models.ManyToManyField(blank=True, null=True, related_name='blocked_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField(max_length=250)),
                ('file', models.FileField(upload_to='files/')),
                ('date_created', models.DateField(auto_now=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogPosts.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogPosts.customuser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogPosts.post')),
            ],
        ),
    ]
