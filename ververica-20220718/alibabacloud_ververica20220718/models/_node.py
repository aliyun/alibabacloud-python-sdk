# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Node(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        connector: str = None,
        database_name: str = None,
        id: str = None,
        is_temporary: bool = None,
        tables: List[main_models.LineageTable] = None,
    ):
        # The name of the catalog.
        self.catalog_name = catalog_name
        # The name of the connector.
        self.connector = connector
        # The name of the database.
        self.database_name = database_name
        # The ID of the node.
        self.id = id
        # Specifies whether the table is a temporary table.
        self.is_temporary = is_temporary
        # The information about the table.
        self.tables = tables

    def validate(self):
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name

        if self.connector is not None:
            result['connector'] = self.connector

        if self.database_name is not None:
            result['databaseName'] = self.database_name

        if self.id is not None:
            result['id'] = self.id

        if self.is_temporary is not None:
            result['isTemporary'] = self.is_temporary

        result['tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['tables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')

        if m.get('connector') is not None:
            self.connector = m.get('connector')

        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isTemporary') is not None:
            self.is_temporary = m.get('isTemporary')

        self.tables = []
        if m.get('tables') is not None:
            for k1 in m.get('tables'):
                temp_model = main_models.LineageTable()
                self.tables.append(temp_model.from_map(k1))

        return self

