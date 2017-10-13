# -*- coding: utf-8 -*-


from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server_device',
            name='admin',
            field=models.ForeignKey(verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_device',
            name='idc',
            field=models.ForeignKey(blank=True, to='cmdb.IDC', max_length=255, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x88\xbf\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_device',
            name='role',
            field=models.ManyToManyField(to='cmdb.Server_Role', verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_device',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe6\x9c\xba\xe5\x99\xa8\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u4e0b\u7ebf'), (1, '\u5728\u7ebf'), (2, '\u5f85\u4e0a\u7ebf'), (3, '\u6d4b\u8bd5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_group',
            name='project',
            field=models.ForeignKey(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0', to='cmdb.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_role',
            name='group',
            field=models.ForeignKey(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xbb\x84', to='cmdb.Server_Group'),
            preserve_default=True,
        ),
    ]
