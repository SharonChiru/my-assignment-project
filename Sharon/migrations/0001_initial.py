# Generated by Django 5.0 on 2023-12-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('programming', models.TextField()),
            ],
        ),
    ]
