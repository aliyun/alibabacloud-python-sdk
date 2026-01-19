# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribePluginSchemasResponseBody(DaraModel):
    def __init__(
        self,
        plugin_schemas: main_models.DescribePluginSchemasResponseBodyPluginSchemas = None,
        request_id: str = None,
    ):
        self.plugin_schemas = plugin_schemas
        self.request_id = request_id

    def validate(self):
        if self.plugin_schemas:
            self.plugin_schemas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plugin_schemas is not None:
            result['PluginSchemas'] = self.plugin_schemas.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginSchemas') is not None:
            temp_model = main_models.DescribePluginSchemasResponseBodyPluginSchemas()
            self.plugin_schemas = temp_model.from_map(m.get('PluginSchemas'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePluginSchemasResponseBodyPluginSchemas(DaraModel):
    def __init__(
        self,
        plugin_schema: List[main_models.DescribePluginSchemasResponseBodyPluginSchemasPluginSchema] = None,
    ):
        self.plugin_schema = plugin_schema

    def validate(self):
        if self.plugin_schema:
            for v1 in self.plugin_schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PluginSchema'] = []
        if self.plugin_schema is not None:
            for k1 in self.plugin_schema:
                result['PluginSchema'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plugin_schema = []
        if m.get('PluginSchema') is not None:
            for k1 in m.get('PluginSchema'):
                temp_model = main_models.DescribePluginSchemasResponseBodyPluginSchemasPluginSchema()
                self.plugin_schema.append(temp_model.from_map(k1))

        return self

class DescribePluginSchemasResponseBodyPluginSchemasPluginSchema(DaraModel):
    def __init__(
        self,
        description: str = None,
        document_id: str = None,
        name: str = None,
        support_classic: bool = None,
        title: str = None,
    ):
        self.description = description
        self.document_id = document_id
        self.name = name
        self.support_classic = support_classic
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.name is not None:
            result['Name'] = self.name

        if self.support_classic is not None:
            result['SupportClassic'] = self.support_classic

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SupportClassic') is not None:
            self.support_classic = m.get('SupportClassic')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

