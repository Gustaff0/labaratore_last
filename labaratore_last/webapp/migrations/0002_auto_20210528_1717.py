# Generated by Django 3.2.3 on 2021-05-28 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='rating',
        ),
        migrations.CreateModel(
            name='QuoteRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote', to='webapp.quote', verbose_name='Цитата')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='rating',
            field=models.ManyToManyField(related_name='rating', through='webapp.QuoteRating', to=settings.AUTH_USER_MODEL),
        ),
    ]
