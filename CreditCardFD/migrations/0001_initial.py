# Generated by Django 3.1.8 on 2021-11-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('uploadfile', models.FileField(null=True, upload_to='media/')),
                ('description', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'CreditCardFD_upload1',
            },
        ),
    ]
