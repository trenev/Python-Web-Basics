# Generated by Django 4.0.2 on 2022-02-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('book_image', models.URLField()),
                ('type', models.CharField(max_length=30)),
            ],
        ),
    ]
