# Generated by Django 4.2.3 on 2023-09-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hom_login', models.CharField(max_length=50)),
                ('hom_gallery', models.CharField(max_length=50)),
            ],
        ),
    ]
