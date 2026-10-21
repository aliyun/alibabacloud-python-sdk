# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgenticDatabaseObject(DaraModel):
    def __init__(
        self,
        database_qualified_name: str = None,
        database_uuid: str = None,
        ddl_sql: str = None,
        object_name: str = None,
        object_qualified_name: str = None,
        object_type: str = None,
    ):
        self.database_qualified_name = database_qualified_name
        self.database_uuid = database_uuid
        self.ddl_sql = ddl_sql
        self.object_name = object_name
        self.object_qualified_name = object_qualified_name
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_qualified_name is not None:
            result['DatabaseQualifiedName'] = self.database_qualified_name

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_qualified_name is not None:
            result['ObjectQualifiedName'] = self.object_qualified_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseQualifiedName') is not None:
            self.database_qualified_name = m.get('DatabaseQualifiedName')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectQualifiedName') is not None:
            self.object_qualified_name = m.get('ObjectQualifiedName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

