# Generated by Django 3.0.3 on 2020-09-12 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('itemlink', models.CharField(max_length=200)),
                ('categ', models.CharField(max_length=100)),
            ],
        ),
    ]