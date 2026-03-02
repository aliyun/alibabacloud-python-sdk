# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TableMeta(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name

        if self.database_name is not None:
            result['databaseName'] = self.database_name

        if self.table_name is not None:
            result['tableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')

        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        return self

