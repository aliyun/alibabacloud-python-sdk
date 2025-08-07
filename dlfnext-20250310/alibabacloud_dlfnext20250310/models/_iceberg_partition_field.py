# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class IcebergPartitionField(DaraModel):
    def __init__(
        self,
        field_id: int = None,
        name: str = None,
        source_id: int = None,
        transform: str = None,
    ):
        self.field_id = field_id
        self.name = name
        self.source_id = source_id
        self.transform = transform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_id is not None:
            result['fieldId'] = self.field_id

        if self.name is not None:
            result['name'] = self.name

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.transform is not None:
            result['transform'] = self.transform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldId') is not None:
            self.field_id = m.get('fieldId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('transform') is not None:
            self.transform = m.get('transform')

        return self

