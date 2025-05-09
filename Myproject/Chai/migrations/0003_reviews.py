# Generated by Django 5.1.7 on 2025-04-06 17:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chai', '0002_alter_chaivarity_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('review', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('chai_varity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Chai.chaivarity')),
            ],
        ),
    ]
