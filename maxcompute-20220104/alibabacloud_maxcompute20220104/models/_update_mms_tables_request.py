# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateMmsTablesRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        dst_project_name: str = None,
        dst_schema_name: str = None,
        status: str = None,
        table_names: List[str] = None,
        tables: List[int] = None,
    ):
        self.db_name = db_name
        self.dst_project_name = dst_project_name
        self.dst_schema_name = dst_schema_name
        self.status = status
        self.table_names = table_names
        # Deprecated
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.dst_project_name is not None:
            result['dstProjectName'] = self.dst_project_name

        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name

        if self.status is not None:
            result['status'] = self.status

        if self.table_names is not None:
            result['tableNames'] = self.table_names

        if self.tables is not None:
            result['tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('dstProjectName') is not None:
            self.dst_project_name = m.get('dstProjectName')

        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tableNames') is not None:
            self.table_names = m.get('tableNames')

        if m.get('tables') is not None:
            self.tables = m.get('tables')

        return self

