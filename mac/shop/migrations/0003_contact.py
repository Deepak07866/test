# Generated by Django 3.0.7 on 2020-06-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200618_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
