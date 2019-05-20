# Generated by Django 2.2.1 on 2019-05-20 15:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0008_city_timezone'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=150)),
                ('date_create_profile', models.DateTimeField(default=django.utils.timezone.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='cities_light.City')),
            ],
        ),
    ]