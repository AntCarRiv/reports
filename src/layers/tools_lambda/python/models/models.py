from peewee import *

from .basemodel import BaseModel


class Groups(BaseModel):
    name = CharField()
    create_at = DateTimeField()
    create_by = CharField(null=True)
    modify_at = DateTimeField(null=True)
    modify_by = CharField(null=True)

    class Meta:
        table_name = 'groups'
        schema = 'demo'


class Clients(BaseModel):
    names = CharField()
    last_name = CharField()
    telephone = CharField(null=True)
    email = CharField(null=True)
    group = ForeignKeyField(column_name='group_id', field='id', model=Groups, null=True)
    create_at = DateTimeField()
    modify_at = DateTimeField(null=True)
    create_by = CharField(null=True)
    modify_by = CharField(null=True)

    class Meta:
        table_name = 'clients'
        schema = 'demo'


class Reports(BaseModel):
    name = CharField()
    bucket = CharField()
    key_s3 = CharField(null=True)
    group = ForeignKeyField(column_name='group_id', field='id', model=Groups, null=True)
    create_at = DateTimeField()
    create_by = CharField(null=True)
    modify_at = DateTimeField(null=True)
    modify_by = CharField(null=True)

    class Meta:
        table_name = 'reports'
        schema = 'demo'


class Documents(BaseModel):
    bucket = CharField()
    key_s3 = CharField()
    client = ForeignKeyField(column_name='client_id', field='id', model=Clients)
    group = ForeignKeyField(column_name='group_id', field='id', model=Groups, null=True)
    report = ForeignKeyField(column_name='report_id', field='id', model=Reports, null=True)
    create_at = DateTimeField()
    create_by = CharField(null=True)
    modify_at = DateTimeField(null=True)
    modify_by = CharField(null=True)

    class Meta:
        table_name = 'documents'
        schema = 'demo'
