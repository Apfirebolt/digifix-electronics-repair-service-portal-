# Generated by Django 3.0.8 on 2020-07-26 23:22

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
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('is_resolved', models.BooleanField(default=False)),
                ('has_issues', models.BooleanField(default=False)),
                ('assigned_engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Complaints',
            },
        ),
        migrations.CreateModel(
            name='ReportIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('reported_at', models.DateTimeField(auto_now=True)),
                ('related_complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_issues', to='complaints.Complaint')),
            ],
            options={
                'verbose_name_plural': 'Complaint Issues',
            },
        ),
        migrations.CreateModel(
            name='ComplaintImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gadget_image', models.ImageField(upload_to='complaint_images')),
                ('image_description', models.TextField()),
                ('related_complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_images', to='complaints.Complaint')),
            ],
            options={
                'verbose_name_plural': 'Complaint Images',
            },
        ),
    ]
