# Generated by Django 3.0.8 on 2020-07-28 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaints', '0004_auto_20200728_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='assigned_engineer',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(groups__name='Engineers'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to=settings.AUTH_USER_MODEL),
        ),
    ]
