# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 


class DataField(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        type: main_models.FullDataType = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        if self.type:
            self.type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            temp_model = main_models.FullDataType()
            self.type = temp_model.from_map(m.get('type'))

        return self

