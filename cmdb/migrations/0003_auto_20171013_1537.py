# -*- coding: utf-8 -*-


from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20171012_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server_device',
            name='admin',
            field=models.ForeignKey(verbose_name='管理员', to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_device',
            name='idc',
            field=models.ForeignKey(verbose_name='机房名称', null=True, to='cmdb.IDC', blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_device',
            name='role',
            field=models.ManyToManyField(to='cmdb.Server_Role', verbose_name='角色', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_device',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, '下线'), (1, '在线'), (2, '待上线'), (3, '测试')], verbose_name='机器状态'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_group',
            name='project',
            field=models.ForeignKey(verbose_name='项目名称', to='cmdb.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server_role',
            name='group',
            field=models.ForeignKey(verbose_name='项目组', to='cmdb.Server_Group'),
            preserve_default=True,
        ),
    ]
