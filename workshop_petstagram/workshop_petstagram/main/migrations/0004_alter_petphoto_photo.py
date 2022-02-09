# Generated by Django 4.0.2 on 2022-02-09 15:42

from django.db import migrations, models
import workshop_petstagram.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_petphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[workshop_petstagram.main.validators.validate_file_max_size_in_mb]),
        ),
    ]