# Generated by Django 3.0.8 on 2020-07-29 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complaints', '0005_auto_20200728_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTestimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Testimonial Content')),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('service_rating', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Service Ratings')),
                ('written_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_testimonial', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Testimonials',
            },
        ),
    ]
