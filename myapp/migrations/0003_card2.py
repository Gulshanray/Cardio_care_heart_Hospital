# Generated by Django 4.2.4 on 2023-09-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_card1'),
    ]

    operations = [
        migrations.CreateModel(
            name='card2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('sub_title', models.CharField(max_length=50, verbose_name='sub_title')),
                ('docu', models.FileField(max_length=255, upload_to='images/')),
            ],
        ),
    ]
