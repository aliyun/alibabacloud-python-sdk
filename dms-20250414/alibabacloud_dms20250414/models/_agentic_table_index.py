# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AgenticTableIndex(DaraModel):
    def __init__(
        self,
        column_names: List[str] = None,
        description: str = None,
        index_name: str = None,
        index_type: str = None,
        primary: bool = None,
        real_column_names: List[str] = None,
        unique: bool = None,
    ):
        # The list of fields included in the index. Fields with a specified prefix length include a length expression, such as name(10).
        self.column_names = column_names
        # The index description.
        self.description = description
        # The index name.
        self.index_name = index_name
        # The index type. Valid values:
        # 
        # - **Primary**: primary key index
        # - **Unique**: unique index
        # - **Normal**: normal index
        # - **FullText**: full-text index
        # - **Spatial**: spatial index
        self.index_type = index_type
        # Specifies whether the index is a primary key index.
        self.primary = primary
        # The list of actual field names referenced by the index, with prefix length expressions removed from ColumnNames.
        self.real_column_names = real_column_names
        # Specifies whether the index is a unique index.
        self.unique = unique

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

        if self.primary is not None:
            result['Primary'] = self.primary

        if self.real_column_names is not None:
            result['RealColumnNames'] = self.real_column_names

        if self.unique is not None:
            result['Unique'] = self.unique

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

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('RealColumnNames') is not None:
            self.real_column_names = m.get('RealColumnNames')

        if m.get('Unique') is not None:
            self.unique = m.get('Unique')

        return self

