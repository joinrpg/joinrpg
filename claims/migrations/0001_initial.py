# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_extensions.db.fields
import jsonfield.fields
import django.utils.timezone
import jrlib.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('first_name', models.CharField(null=True, max_length=255)),
                ('second_name', models.CharField(null=True, max_length=255)),
                ('patronymic', models.CharField(null=True, max_length=255)),
                ('nick', models.CharField(null=True, max_length=255)),
                ('email', models.EmailField(null=True, max_length=75)),
                ('username', models.CharField(unique=True, max_length=42)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressCity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AddressRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(to='claims.AddressCountry')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthenticationSystem',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(serialize=False, primary_key=True, max_length=255)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClaimComment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('claim', models.ForeignKey(to='claims.Claim')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClaimHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('claim', models.ForeignKey(to='claims.Claim')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1023)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ObjectHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('obj', models.ForeignKey(to='claims.Object')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Название игры (проекта)', max_length=1023)),
                ('external_uri', models.URLField(null=True, verbose_name='Сссылка на сайт игры', blank=True, max_length=255)),
                ('description', models.TextField(null=True, verbose_name='Описание игры (для игроков)', blank=True)),
                ('kogdaigra_link', jrlib.models.KogdaIgraField(null=True, verbose_name='Ссылка на профиль на КогдаИгре', blank=True)),
                ('game_begin_date', models.DateField(verbose_name='Дата начала игры')),
                ('game_end_date', models.DateField(verbose_name='Дата конца игры')),
                ('vk_club', jrlib.models.VKField(null=True)),
                ('lj_comm', jrlib.models.LiveJournalField(null=True, blank=True)),
                ('facebook', jrlib.models.FacebookField(null=True, blank=True)),
                ('twitter', jrlib.models.TwitterField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectAcl',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('can_change_player_fields', models.BooleanField(default=True)),
                ('can_write_comments', models.BooleanField(default=True)),
                ('can_accept_money', models.BooleanField(default=True)),
                ('can_setup_fields', models.BooleanField(default=False)),
                ('can_grant_acl', models.BooleanField(default=True)),
                ('project', models.ForeignKey(to='claims.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectField',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('project', models.ForeignKey(to='claims.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFieldGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('project', models.ForeignKey(to='claims.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('project_field', models.ForeignKey(to='claims.ProjectField')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True, help_text='Может ли мастер менять что-то в проекте или он уже ушел в архив')),
                ('is_visible', models.BooleanField(default=False, help_text='Может ли игрок увидеть проект во всяких «куда заявиться»')),
                ('can_add_new_claim', models.BooleanField(default=False, help_text='Могут ли игроки добавлять новые заявки или они закрыты (уже/еще)')),
                ('can_player_change_character', models.BooleanField(default=False, help_text='Могут ли игроки что-то менять в персонаже или мастера заморозили заявки к выезду на полигон')),
                ('is_default_status', models.BooleanField(default=False, verbose_name='Статус для вновь созданных игр', help_text='Да, если этот статус выставляется проекту при создании')),
            ],
            options={
                'verbose_name': 'Статус проектов',
                'verbose_name_plural': 'Статусы проектов',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('obj', models.ForeignKey(to='claims.Object')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryPieceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('story_piece', models.ForeignKey(to='claims.StoryPiece')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('guid', django_extensions.db.fields.UUIDField(name='guid', editable=False, db_index=True, blank=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('up_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectfield',
            name='project_field_group',
            field=models.ForeignKey(to='claims.ProjectFieldGroup', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(to='claims.ProjectStatus', verbose_name='Статус проекта'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='object',
            name='project',
            field=models.ForeignKey(to='claims.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='claim',
            name='obj',
            field=models.ForeignKey(to='claims.Object'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authentication',
            name='system',
            field=models.ForeignKey(to='claims.AuthenticationSystem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authentication',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='addresscity',
            name='region',
            field=models.ForeignKey(to='claims.AddressRegion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(to='claims.AddressCity', null=True),
            preserve_default=True,
        ),
    ]
