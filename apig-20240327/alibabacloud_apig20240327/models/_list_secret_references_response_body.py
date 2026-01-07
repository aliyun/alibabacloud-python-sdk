# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListSecretReferencesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListSecretReferencesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = main_models.ListSecretReferencesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListSecretReferencesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListSecretReferencesResponseBodyDataItems] = None,
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
                temp_model = main_models.ListSecretReferencesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListSecretReferencesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        plugin_config: main_models.ListSecretReferencesResponseBodyDataItemsPluginConfig = None,
        service_config: main_models.ListSecretReferencesResponseBodyDataItemsServiceConfig = None,
        consumer_config: main_models.ListSecretReferencesResponseBodyDataItemsConsumerConfig = None,
        gateway_id: str = None,
        mcp_server_config: main_models.ListSecretReferencesResponseBodyDataItemsMcpServerConfig = None,
        resource_type: str = None,
    ):
        self.plugin_config = plugin_config
        self.service_config = service_config
        self.consumer_config = consumer_config
        self.gateway_id = gateway_id
        self.mcp_server_config = mcp_server_config
        self.resource_type = resource_type

    def validate(self):
        if self.plugin_config:
            self.plugin_config.validate()
        if self.service_config:
            self.service_config.validate()
        if self.consumer_config:
            self.consumer_config.validate()
        if self.mcp_server_config:
            self.mcp_server_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plugin_config is not None:
            result['PluginConfig'] = self.plugin_config.to_map()

        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config.to_map()

        if self.consumer_config is not None:
            result['consumerConfig'] = self.consumer_config.to_map()

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.mcp_server_config is not None:
            result['mcpServerConfig'] = self.mcp_server_config.to_map()

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginConfig') is not None:
            temp_model = main_models.ListSecretReferencesResponseBodyDataItemsPluginConfig()
            self.plugin_config = temp_model.from_map(m.get('PluginConfig'))

        if m.get('ServiceConfig') is not None:
            temp_model = main_models.ListSecretReferencesResponseBodyDataItemsServiceConfig()
            self.service_config = temp_model.from_map(m.get('ServiceConfig'))

        if m.get('consumerConfig') is not None:
            temp_model = main_models.ListSecretReferencesResponseBodyDataItemsConsumerConfig()
            self.consumer_config = temp_model.from_map(m.get('consumerConfig'))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('mcpServerConfig') is not None:
            temp_model = main_models.ListSecretReferencesResponseBodyDataItemsMcpServerConfig()
            self.mcp_server_config = temp_model.from_map(m.get('mcpServerConfig'))

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class ListSecretReferencesResponseBodyDataItemsMcpServerConfig(DaraModel):
    def __init__(
        self,
        http_api_id: str = None,
        name: str = None,
        route_id: str = None,
    ):
        self.http_api_id = http_api_id
        self.name = name
        self.route_id = route_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id

        if self.name is not None:
            result['name'] = self.name

        if self.route_id is not None:
            result['routeId'] = self.route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        return self

class ListSecretReferencesResponseBodyDataItemsConsumerConfig(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        name: str = None,
    ):
        self.consumer_id = consumer_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListSecretReferencesResponseBodyDataItemsServiceConfig(DaraModel):
    def __init__(
        self,
        name: str = None,
        service_id: str = None,
    ):
        self.name = name
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

class ListSecretReferencesResponseBodyDataItemsPluginConfig(DaraModel):
    def __init__(
        self,
        name: str = None,
        plugin_class_id: str = None,
        plugin_id: str = None,
    ):
        self.name = name
        self.plugin_class_id = plugin_class_id
        self.plugin_id = plugin_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        return self

