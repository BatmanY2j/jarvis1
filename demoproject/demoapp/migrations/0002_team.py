# Generated by Django 4.2.1 on 2023-05-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=15)),
                ('im', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
        ),
    ]