# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class DataSource(DaraModel):
    def __init__(
        self,
        fields: List[Dict[str, str]] = None,
        key_field: str = None,
        parameters: Dict[str, Any] = None,
        plugins: Dict[str, main_models.DataSourcePluginsValue] = None,
        schema_name: str = None,
        table_name: str = None,
        type: str = None,
    ):
        self.fields = fields
        self.key_field = key_field
        self.parameters = parameters
        self.plugins = plugins
        self.schema_name = schema_name
        self.table_name = table_name
        self.type = type

    def validate(self):
        if self.plugins:
            for v1 in self.plugins.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['fields'] = self.fields

        if self.key_field is not None:
            result['keyField'] = self.key_field

        if self.parameters is not None:
            result['parameters'] = self.parameters

        result['plugins'] = {}
        if self.plugins is not None:
            for k1, v1 in self.plugins.items():
                result['plugins'][k1] = v1.to_map() if v1 else None

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('keyField') is not None:
            self.key_field = m.get('keyField')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        self.plugins = {}
        if m.get('plugins') is not None:
            for k1, v1 in m.get('plugins').items():
                temp_model = main_models.DataSourcePluginsValue()
                self.plugins[k1] = temp_model.from_map(v1)

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

