# Generated by Django 3.0.8 on 2020-07-07 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='English', help_text='Enter written language of book', max_length=100),
        ),
    ]
