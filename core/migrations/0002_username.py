# Generated by Django 3.1.13 on 2021-11-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('email', models.EmailField(max_length=1000)),
                ('phone_number', models.IntegerField()),
                ('adderss', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
