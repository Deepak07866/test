# Generated by Django 3.0.7 on 2020-07-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('decs', models.CharField(default='', max_length=300)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
