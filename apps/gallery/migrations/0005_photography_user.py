# Generated by Django 4.2.3 on 2023-07-17 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0004_alter_photography_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photography_user', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
