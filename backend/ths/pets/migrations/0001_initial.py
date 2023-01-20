# Generated by Django 3.2.16 on 2023-01-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('animal_type', models.CharField(choices=[('Cat', 'cat'), ('Dog', 'dog'), ('Fish', 'fish'), ('Rabbit', 'rabbit')], max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
