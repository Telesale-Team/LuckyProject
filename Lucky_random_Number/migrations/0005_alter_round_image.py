# Generated by Django 3.2 on 2023-10-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lucky_random_Number', '0004_alter_round_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='media/image_tauthong'),
        ),
    ]
