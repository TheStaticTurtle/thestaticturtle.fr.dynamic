# Generated by Django 3.2.5 on 2021-07-25 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20210726_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='did_at_school',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.school'),
        ),
        migrations.AddField(
            model_name='project',
            name='download_url',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
