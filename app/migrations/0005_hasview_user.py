# Generated by Django 3.0.7 on 2020-08-12 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200812_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='主键id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('unionid', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='百度unionid')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HasView',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False, verbose_name='主键id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.News', verbose_name='新闻')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='用户')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
