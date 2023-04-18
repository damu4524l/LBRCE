# Generated by Django 4.1.8 on 2023-04-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_id', models.CharField(max_length=30)),
                ('student_number', models.IntegerField(max_length=10)),
                ('student_collage', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('feedback', models.CharField(max_length=200)),
            ],
        ),
    ]
