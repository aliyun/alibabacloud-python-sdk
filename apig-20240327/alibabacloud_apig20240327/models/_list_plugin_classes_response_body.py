# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListPluginClassesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListPluginClassesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListPluginClassesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListPluginClassesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListPluginClassesResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_size is not None:
            result['totalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListPluginClassesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListPluginClassesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        installed: bool = None,
        name: str = None,
        plugin_class_id: str = None,
        plugin_id: str = None,
        publish_status: str = None,
        source: str = None,
        supported_min_gateway_version: str = None,
        type: str = None,
        version: str = None,
    ):
        self.alias = alias
        self.description = description
        self.installed = installed
        self.name = name
        self.plugin_class_id = plugin_class_id
        self.plugin_id = plugin_id
        self.publish_status = publish_status
        self.source = source
        self.supported_min_gateway_version = supported_min_gateway_version
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.description is not None:
            result['description'] = self.description

        if self.installed is not None:
            result['installed'] = self.installed

        if self.name is not None:
            result['name'] = self.name

        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.publish_status is not None:
            result['publishStatus'] = self.publish_status

        if self.source is not None:
            result['source'] = self.source

        if self.supported_min_gateway_version is not None:
            result['supportedMinGatewayVersion'] = self.supported_min_gateway_version

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('installed') is not None:
            self.installed = m.get('installed')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('publishStatus') is not None:
            self.publish_status = m.get('publishStatus')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('supportedMinGatewayVersion') is not None:
            self.supported_min_gateway_version = m.get('supportedMinGatewayVersion')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

