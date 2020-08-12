# coding: utf8
from uuid import uuid4
import json

from django.db import models
from django.core import serializers
from datetime import datetime


class IdModel(models.Model):
    id = models.AutoField('主键id', max_length=11, primary_key=True)
    created_at = models.DateTimeField('创建时间', null=False, auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', null=False, auto_now=True)
    objects = models.Manager()

    def created_at_str(self, fmt='%Y-%m-%d %H:%M:%S'):
        return datetime.strftime(self.created_at, fmt) if self.created_at else ''

    def created_on_str(self, fmt='%Y-%m-%d'):
        dt = getattr(self, 'created_on', None) or self.created_at
        return datetime.strftime(dt, fmt) if dt else ''

    def updated_on_str(self, fmt='%Y-%m-%d'):
        dt = getattr(self, 'updated_on', None) or self.updated_at
        return datetime.strftime(dt, fmt) if dt else ''

    def updated_at_str(self, fmt='%Y-%m-%d %H:%M:%S'):
        return datetime.strftime(self.updated_at, fmt) if self.updated_at else ''

    def to_dict(self, ext_props=[], exc_props=[]):
        serial_obj = serializers.serialize('json', [self])
        obj_as_dict = json.loads(serial_obj)[0]['fields']
        ext_props.extend(['id'])
        for k in ext_props:
            method_or_prop = getattr(self, k, None)
            if method_or_prop:
                if callable(method_or_prop):
                    method_or_prop = method_or_prop()
            obj_as_dict[k] = method_or_prop
        exc_props.extend(['created_at', 'updated_at'])
        for k in exc_props:
            if k in obj_as_dict:
                del obj_as_dict[k]
        return obj_as_dict

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    id = models.CharField('ID', primary_key=True, max_length=32, null=False, default=uuid4().hex)
    created_at = models.DateTimeField('创建时间', null=False, auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', null=False, auto_now=True)
    objects = models.Manager()

    def created_at_str(self, fmt='%Y-%m-%d %H:%M:%S'):
        return datetime.strftime(self.created_at, fmt) if self.created_at else ''

    def created_on_str(self, fmt='%Y-%m-%d'):
        dt = getattr(self, 'created_on', None) or self.created_at
        return datetime.strftime(dt, fmt) if dt else ''

    def updated_on_str(self, fmt='%Y-%m-%d'):
        dt = getattr(self, 'updated_on', None) or self.updated_at
        return datetime.strftime(dt, fmt) if dt else ''

    def updated_at_str(self, fmt='%Y-%m-%d %H:%M:%S'):
        return datetime.strftime(self.updated_at, fmt) if self.updated_at else ''

    def to_dict(self, ext_props=[], exc_props=[]):
        serial_obj = serializers.serialize('json', [self])
        obj_as_dict = json.loads(serial_obj)[0]['fields']
        ext_props.extend(['id', 'created_on_str', 'created_at_str'])
        for k in ext_props:
            method_or_prop = getattr(self, k, None)
            if method_or_prop:
                if callable(method_or_prop):
                    method_or_prop = method_or_prop()
            obj_as_dict[k] = method_or_prop
        exc_props.extend(['created_at', 'updated_at'])
        for k in exc_props:
            if k in obj_as_dict:
                del obj_as_dict[k]
        return obj_as_dict

    class Meta:
        abstract = True
