# Generated by Django 2.2.12 on 2024-04-28 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('author', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='authors.Author')),
            ],
        ),
    ]
