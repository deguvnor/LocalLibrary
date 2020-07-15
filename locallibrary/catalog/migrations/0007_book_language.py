# Generated by Django 3.0.7 on 2020-07-15 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200715_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Choose written language of book', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]