# Generated by Django 2.0.3 on 2018-04-24 15:55

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostRedactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_redactor', models.CharField(max_length=30)),
                ('short_text', redactor.fields.RedactorField(verbose_name='Text')),
            ],
        ),
    ]