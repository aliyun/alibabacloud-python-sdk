# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OneMetaTableIndex(DaraModel):
    def __init__(
        self,
        column_names: List[str] = None,
        description: str = None,
        index_name: str = None,
        index_type: str = None,
    ):
        self.column_names = column_names
        self.description = description
        self.index_name = index_name
        self.index_type = index_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names

        if self.description is not None:
            result['Description'] = self.description

        if self.index_name is not None:
            result['IndexName'] = self.index_name

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        return self

