# -*- coding: utf-8 -*-


from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='IDC名称', max_length=255, unique=True)),
                ('memo', models.CharField(verbose_name='备注', blank=True, max_length=255)),
            ],
            options={
                'db_table': 'idc',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='项目名称', max_length=255, unique=True)),
                ('memo', models.CharField(verbose_name='备注', blank=True, max_length=255)),
            ],
            options={
                'db_table': 'project',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server_Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='主机名称', max_length=100, unique=True)),
                ('sn', models.CharField(verbose_name='SN号', blank=True, max_length=200)),
                ('public_ip', models.CharField(verbose_name='外网IP', blank=True, max_length=200)),
                ('private_ip', models.CharField(verbose_name='内网IP', blank=True, max_length=200)),
                ('mac', models.CharField(verbose_name='MAC地址', blank=True, max_length=200)),
                ('os', models.CharField(verbose_name='操作系统', blank=True, max_length=200)),
                ('disk', models.CharField(verbose_name='磁盘', blank=True, max_length=200)),
                ('mem', models.CharField(verbose_name='内存', blank=True, max_length=200)),
                ('cpu', models.CharField(verbose_name='CPU', blank=True, max_length=200)),
                ('status', models.SmallIntegerField(verbose_name='机器状态', choices=[(0, '下线'), (1, '在线'), (2, '待上线'), (3, '测试')], default=1)),
                ('memo', models.CharField(verbose_name='备注', blank=True, max_length=200)),
                ('admin', models.ForeignKey(verbose_name='管理员', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('idc', models.ForeignKey(verbose_name='机房名称', blank=True, max_length=255, to='cmdb.IDC', null=True)),
            ],
            options={
                'db_table': 'server_device',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='主机组', max_length=255, unique=True)),
                ('memo', models.CharField(verbose_name='备注', blank=True, max_length=255)),
                ('project', models.ForeignKey(verbose_name='项目名称', to='cmdb.Project')),
            ],
            options={
                'db_table': 'server_group',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='角色', max_length=255)),
                ('memo', models.CharField(verbose_name='备注', blank=True, max_length=255)),
                ('group', models.ForeignKey(verbose_name='项目组', to='cmdb.Server_Group')),
            ],
            options={
                'db_table': 'server_role',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='server_role',
            unique_together=set([('name', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='server_group',
            unique_together=set([('name', 'project')]),
        ),
        migrations.AddField(
            model_name='server_device',
            name='role',
            field=models.ManyToManyField(to='cmdb.Server_Role', verbose_name='角色', blank=True),
            preserve_default=True,
        ),
    ]
