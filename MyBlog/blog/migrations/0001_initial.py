# Generated by Django 2.0.3 on 2018-04-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.CharField(max_length=30)),
                ('content_post', models.TextField()),
                ('date_post', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
