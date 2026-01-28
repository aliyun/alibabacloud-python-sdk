# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class OneMetaTableColumn(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_type: str = None,
        description: str = None,
        engine_meta: main_models.OneMetaTableColumnEngineMeta = None,
        position: int = None,
    ):
        self.column_name = column_name
        self.column_type = column_type
        self.description = description
        self.engine_meta = engine_meta
        self.position = position

    def validate(self):
        if self.engine_meta:
            self.engine_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.description is not None:
            result['Description'] = self.description

        if self.engine_meta is not None:
            result['EngineMeta'] = self.engine_meta.to_map()

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineMeta') is not None:
            temp_model = main_models.OneMetaTableColumnEngineMeta()
            self.engine_meta = temp_model.from_map(m.get('EngineMeta'))

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

