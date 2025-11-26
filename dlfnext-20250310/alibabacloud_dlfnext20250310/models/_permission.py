# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class Permission(DaraModel):
    def __init__(
        self,
        access: str = None,
        columns: main_models.PermissionColumns = None,
        database: str = None,
        expire_time: str = None,
        function: str = None,
        principal: str = None,
        resource_type: str = None,
        table: str = None,
        view: str = None,
    ):
        self.access = access
        self.columns = columns
        self.database = database
        self.expire_time = expire_time
        self.function = function
        self.principal = principal
        self.resource_type = resource_type
        self.table = table
        self.view = view

    def validate(self):
        if self.columns:
            self.columns.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access is not None:
            result['access'] = self.access

        if self.columns is not None:
            result['columns'] = self.columns.to_map()

        if self.database is not None:
            result['database'] = self.database

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.function is not None:
            result['function'] = self.function

        if self.principal is not None:
            result['principal'] = self.principal

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.table is not None:
            result['table'] = self.table

        if self.view is not None:
            result['view'] = self.view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access') is not None:
            self.access = m.get('access')

        if m.get('columns') is not None:
            temp_model = main_models.PermissionColumns()
            self.columns = temp_model.from_map(m.get('columns'))

        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('function') is not None:
            self.function = m.get('function')

        if m.get('principal') is not None:
            self.principal = m.get('principal')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('table') is not None:
            self.table = m.get('table')

        if m.get('view') is not None:
            self.view = m.get('view')

        return self



class PermissionColumns(DaraModel):
    def __init__(
        self,
        column_names: List[str] = None,
        excluded_column_names: List[str] = None,
    ):
        self.column_names = column_names
        self.excluded_column_names = excluded_column_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_names is not None:
            result['columnNames'] = self.column_names

        if self.excluded_column_names is not None:
            result['excludedColumnNames'] = self.excluded_column_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnNames') is not None:
            self.column_names = m.get('columnNames')

        if m.get('excludedColumnNames') is not None:
            self.excluded_column_names = m.get('excludedColumnNames')

        return self

