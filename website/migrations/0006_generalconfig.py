# Generated by Django 3.2.5 on 2021-07-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_popover_text_sociallink_tooltip'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
                ('values', models.CharField(max_length=10000)),
            ],
        ),
    ]
