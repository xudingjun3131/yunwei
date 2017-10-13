# -*- coding: utf-8 -*-


from django.db import models, migrations
import echelon.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangelogEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('content_type', models.CharField(db_index=True, verbose_name='content type', max_length=255)),
                ('object_id', models.IntegerField(verbose_name='ID')),
                ('object_str', models.CharField(verbose_name='Object', max_length=100)),
                ('action', models.CharField(verbose_name='Action', max_length=6, choices=[('add', 'Add'), ('change', 'Change'), ('delete', 'Delete')])),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('changes', echelon.fields.ChangelogField(verbose_name='Changes')),
                ('before_change', echelon.fields.ChangelogField(verbose_name='Before Change')),
                ('after_change', echelon.fields.ChangelogField(verbose_name='After Change')),
                ('who', echelon.fields.CurrentUserField(to=settings.AUTH_USER_MODEL, null=True, editable=False)),
            ],
            options={
                'verbose_name_plural': 'changelog entries',
            },
            bases=(models.Model,),
        ),
    ]
