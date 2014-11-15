# -*- coding: utf-8 -*-
from django.db import models
from jrlib.models import JRModel, VKField
import jsonfield
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django_extensions.db.fields import UUIDField

# UserManager

class UserManager(BaseUserManager):
    def __create_user(self, username, is_su=False, password=None):
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(username=username)
        user.is_superuser = is_su
        user.save()
        if password:
            auth_sys = AuthenticationSystem.objects.get(name='local')
            if not auth_sys:
                raise ValueError('There are no \'local\' Authentication system. Please create one first')
            auth = Authentication.objects.create(user=user, system=auth_sys, data = {'password': password})
            auth.save()
        
    def create_user(self, username, password=None):
        self.__create_user(username, False, password)

    def create_superuser(self, username, password):
        if not password:
            raise ValueError('Superuser MUST have a password')
        self.__create_user(username, True, password)
        
# Адрес
class AddressCountry(JRModel):
    name = models.CharField(max_length = 255)
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
    def __str__(self):
        return self.name

class AddressRegion(JRModel):
    country = models.ForeignKey(AddressCountry)
    name = models.CharField(max_length = 255)
    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
    def __str__(self):
        return self.name

class AddressCity(JRModel):
    region = models.ForeignKey(AddressRegion)
    name = models.CharField(max_length = 255)
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
    def __str__(self):
        return self.name

# Пользователь
class User(AbstractBaseUser):
    guid = UUIDField(db_index=True)
    city = models.ForeignKey(AddressCity, null=True)

    first_name = models.CharField(null=True, max_length = 255)
    second_name = models.CharField(null=True, max_length = 255)
    patronymic = models.CharField(null=True, max_length = 255)
    nick = models.CharField(null=True, max_length = 255)
    
    email = models.EmailField(null=True)
    username = models.CharField(unique=True, max_length = 42)

    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def is_admin(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        return self.username
        
#    last_login = models.DateTimeField(auto_now_add=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def check_password(self, raw_password):
        try:
            auth = Authentication.objects.get(user=self, system='local')
        except Authentication.DoesNotExist:
            auth = None

        if auth is None:
            return False
        return auth.data['password'] == raw_password

class AuthenticationSystem(JRModel):
    name = models.CharField(primary_key = True, max_length = 255)
    data = jsonfield.JSONField()

class Authentication(JRModel):
    user = models.ForeignKey(User, related_name='+')
    system = models.ForeignKey(AuthenticationSystem)
    data = jsonfield.JSONField()

# Базовый класс (без создания таблицы) для любых "авторских" 
# таблиц, т.е., у записей которых есть автор из Users

class AuthoredModel(JRModel):
    author = models.ForeignKey(User, related_name='+')
    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

# проект — собсно, игра
class Project(AuthoredModel):
    name = models.CharField(max_length = 1023)
    external_uri = models.URLField(max_length = 255)
    description = models.TextField()
    vk_club = VKField()
    # TODO

# Права доступа к проекту
class ProjectAcl(JRModel):
    project = models.ForeignKey(Project)

# Группы полей заявок в проекте
class ProjectFieldGroup(JRModel):
    project = models.ForeignKey(Project)

# Поля заявки в проекте
class ProjectField(JRModel):
    project = models.ForeignKey(Project)
    project_field_group = models.ForeignKey(ProjectFieldGroup, blank=True, null=True)

# Значения комбобоксов в полях заявок в проекте
class ProjectFieldValue(JRModel):
    project_field = models.ForeignKey(ProjectField)

# Объекты игрового мира — персонажики, группочки персонажиков, локации
class Object(AuthoredModel):
    project = models.ForeignKey(Project)

    name = models.CharField(max_length=1023)

# История изменений в объектах
class ObjectHistory(AuthoredModel):
    obj = models.ForeignKey(Object)

# Подписки пользователей на изменения
class Subscription(AuthoredModel):
    user = models.ForeignKey(User)
    # TODO

# Заявка
class Claim(AuthoredModel):
    obj = models.ForeignKey(Object)

# история изменения заявок
class ClaimHistory(AuthoredModel):
    claim = models.ForeignKey(Claim)

# Комментарии к заявке (переписка)
class ClaimComment(AuthoredModel):
    claim = models.ForeignKey(Claim)

# Загрузы
class StoryPiece(AuthoredModel):
    obj = models.ForeignKey(Object)

# История изменения загрузов
class StoryPieceHistory(AuthoredModel):
    story_piece = models.ForeignKey(StoryPiece)


