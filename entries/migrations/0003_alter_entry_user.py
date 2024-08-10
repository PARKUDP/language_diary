# Generated by Django 5.0.7 on 2024-08-10 06:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def set_default_user(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    Entry = apps.get_model('entries', 'Entry')
    
    # ここで適切なデフォルトユーザーを設定
    default_user = User.objects.first()
    
    if default_user:
        for entry in Entry.objects.filter(user__isnull=True):
            entry.user = default_user
            entry.save()

class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_entry_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
