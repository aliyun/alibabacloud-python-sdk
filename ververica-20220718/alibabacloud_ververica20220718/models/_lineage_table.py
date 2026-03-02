# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class LineageTable(DaraModel):
    def __init__(
        self,
        columns: List[main_models.LineageColumn] = None,
        id: str = None,
        properties: Dict[str, Any] = None,
        table_name: str = None,
        with_: Dict[str, Any] = None,
    ):
        # The information about columns.
        self.columns = columns
        # The table ID.
        self.id = id
        # The information about the table. The information includes the user who creates the table, the user who modifies the table, and the creation time and modification time of the table.
        self.properties = properties
        # The name of the table.
        self.table_name = table_name
        # The parameters of the table.
        self.with_ = with_

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['columns'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['id'] = self.id

        if self.properties is not None:
            result['properties'] = self.properties

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.with_ is not None:
            result['with'] = self.with_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k1 in m.get('columns'):
                temp_model = main_models.LineageColumn()
                self.columns.append(temp_model.from_map(k1))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('with') is not None:
            self.with_ = m.get('with')

        return self

