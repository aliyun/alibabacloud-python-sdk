# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class SchemaTablesValue(DaraModel):
    def __init__(
        self,
        name: str = None,
        primary_table: bool = None,
        fields: Dict[str, main_models.SchemaTablesValueFieldsValue] = None,
    ):
        self.name = name
        self.primary_table = primary_table
        self.fields = fields

    def validate(self):
        if self.fields:
            for v1 in self.fields.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.primary_table is not None:
            result['primaryTable'] = self.primary_table

        result['fields'] = {}
        if self.fields is not None:
            for k1, v1 in self.fields.items():
                result['fields'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('primaryTable') is not None:
            self.primary_table = m.get('primaryTable')

        self.fields = {}
        if m.get('fields') is not None:
            for k1, v1 in m.get('fields').items():
                temp_model = main_models.SchemaTablesValueFieldsValue()
                self.fields[k1] = temp_model.from_map(v1)

        return self

