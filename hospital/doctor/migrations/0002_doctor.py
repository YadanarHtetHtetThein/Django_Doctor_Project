# Generated by Django 3.2.8 on 2021-10-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qualifications', models.TextField()),
                ('duty', models.TextField()),
                ('category', models.IntegerField()),
            ],
        ),
    ]
