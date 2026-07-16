# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeTairSkvDdbTableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tables: main_models.DescribeTairSkvDdbTableResponseBodyTables = None,
    ):
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        self.tables = tables

    def validate(self):
        if self.tables:
            self.tables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tables is not None:
            result['Tables'] = self.tables.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tables') is not None:
            temp_model = main_models.DescribeTairSkvDdbTableResponseBodyTables()
            self.tables = temp_model.from_map(m.get('Tables'))

        return self

class DescribeTairSkvDdbTableResponseBodyTables(DaraModel):
    def __init__(
        self,
        table: List[main_models.DescribeTairSkvDdbTableResponseBodyTablesTable] = None,
    ):
        self.table = table

    def validate(self):
        if self.table:
            for v1 in self.table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Table'] = []
        if self.table is not None:
            for k1 in self.table:
                result['Table'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k1 in m.get('Table'):
                temp_model = main_models.DescribeTairSkvDdbTableResponseBodyTablesTable()
                self.table.append(temp_model.from_map(k1))

        return self

class DescribeTairSkvDdbTableResponseBodyTablesTable(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        connections: int = None,
        table_id: str = None,
        table_name: str = None,
    ):
        self.bandwidth = bandwidth
        self.connections = connections
        self.table_id = table_id
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.connections is not None:
            result['Connections'] = self.connections

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

