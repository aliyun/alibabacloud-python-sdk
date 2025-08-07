# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 
from typing import List


class FullDataType(DaraModel):
    def __init__(
        self,
        element: main_models.FullDataType = None,
        fields: List[main_models.DataField] = None,
        key: main_models.FullDataType = None,
        type: str = None,
        value: main_models.FullDataType = None,
    ):
        self.element = element
        self.fields = fields
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        if self.element:
            self.element.validate()
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()
        if self.key:
            self.key.validate()
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.element is not None:
            result['element'] = self.element.to_map()

        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        if self.key is not None:
            result['key'] = self.key.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('element') is not None:
            temp_model = main_models.FullDataType()
            self.element = temp_model.from_map(m.get('element'))

        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.DataField()
                self.fields.append(temp_model.from_map(k1))

        if m.get('key') is not None:
            temp_model = main_models.FullDataType()
            self.key = temp_model.from_map(m.get('key'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            temp_model = main_models.FullDataType()
            self.value = temp_model.from_map(m.get('value'))

        return self

