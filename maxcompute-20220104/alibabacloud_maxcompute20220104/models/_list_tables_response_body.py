# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListTablesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListTablesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListTablesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListTablesResponseBodyData(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        tables: List[main_models.ListTablesResponseBodyDataTables] = None,
    ):
        self.marker = marker
        self.max_item = max_item
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
        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_item is not None:
            result['maxItem'] = self.max_item

        result['tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['tables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        self.tables = []
        if m.get('tables') is not None:
            for k1 in m.get('tables'):
                temp_model = main_models.ListTablesResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k1))

        return self

class ListTablesResponseBodyDataTables(DaraModel):
    def __init__(
        self,
        creation_time: int = None,
        display_name: str = None,
        name: str = None,
        owner: str = None,
        schema: str = None,
        type: str = None,
    ):
        self.creation_time = creation_time
        self.display_name = display_name
        self.name = name
        self.owner = owner
        self.schema = schema
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.schema is not None:
            result['schema'] = self.schema

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

