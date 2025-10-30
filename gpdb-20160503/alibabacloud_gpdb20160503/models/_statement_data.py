# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StatementData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        database: str = None,
        id: str = None,
        parameters: List[str] = None,
        secret_arn: str = None,
        sql: str = None,
        sqls: List[str] = None,
        status: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.database = database
        self.id = id
        self.parameters = parameters
        self.secret_arn = secret_arn
        self.sql = sql
        self.sqls = sqls
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.database is not None:
            result['Database'] = self.database

        if self.id is not None:
            result['Id'] = self.id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.sqls is not None:
            result['Sqls'] = self.sqls

        if self.status is not None:
            result['Status'] = self.status

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('Sqls') is not None:
            self.sqls = m.get('Sqls')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

