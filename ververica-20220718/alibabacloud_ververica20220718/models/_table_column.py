# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class TableColumn(DaraModel):
    def __init__(
        self,
        expression: str = None,
        logical_type: str = None,
        metadata_info: main_models.MetadataInfo = None,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        # The computed column.
        self.expression = expression
        self.logical_type = logical_type
        # The metadata information.
        self.metadata_info = metadata_info
        # The column name.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether the column can have a null value.
        self.nullable = nullable
        # The data type of the column.
        self.type = type

    def validate(self):
        if self.metadata_info:
            self.metadata_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['expression'] = self.expression

        if self.logical_type is not None:
            result['logicalType'] = self.logical_type

        if self.metadata_info is not None:
            result['metadataInfo'] = self.metadata_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.nullable is not None:
            result['nullable'] = self.nullable

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('logicalType') is not None:
            self.logical_type = m.get('logicalType')

        if m.get('metadataInfo') is not None:
            temp_model = main_models.MetadataInfo()
            self.metadata_info = temp_model.from_map(m.get('metadataInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

