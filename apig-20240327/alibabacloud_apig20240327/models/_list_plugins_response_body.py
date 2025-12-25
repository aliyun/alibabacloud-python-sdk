# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListPluginsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListPluginsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response payload.
        self.data = data
        # The status message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.ListPluginsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListPluginsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListPluginsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The list of plug-in information.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of entries returned.
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
                temp_model = main_models.ListPluginsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListPluginsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        attachment_info: main_models.ListPluginsResponseBodyDataItemsAttachmentInfo = None,
        gateway_info: main_models.ListPluginsResponseBodyDataItemsGatewayInfo = None,
        plugin_class_info: main_models.ListPluginsResponseBodyDataItemsPluginClassInfo = None,
        plugin_id: str = None,
    ):
        # The attachment information.
        self.attachment_info = attachment_info
        # The gateway instance information.
        self.gateway_info = gateway_info
        # The plug-in type information.
        self.plugin_class_info = plugin_class_info
        # The plug-in ID.
        self.plugin_id = plugin_id

    def validate(self):
        if self.attachment_info:
            self.attachment_info.validate()
        if self.gateway_info:
            self.gateway_info.validate()
        if self.plugin_class_info:
            self.plugin_class_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_info is not None:
            result['attachmentInfo'] = self.attachment_info.to_map()

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.plugin_class_info is not None:
            result['pluginClassInfo'] = self.plugin_class_info.to_map()

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachmentInfo') is not None:
            temp_model = main_models.ListPluginsResponseBodyDataItemsAttachmentInfo()
            self.attachment_info = temp_model.from_map(m.get('attachmentInfo'))

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.ListPluginsResponseBodyDataItemsGatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('pluginClassInfo') is not None:
            temp_model = main_models.ListPluginsResponseBodyDataItemsPluginClassInfo()
            self.plugin_class_info = temp_model.from_map(m.get('pluginClassInfo'))

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        return self

class ListPluginsResponseBodyDataItemsPluginClassInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        plugin_class_id: str = None,
        source: str = None,
        version: str = None,
        version_description: str = None,
    ):
        # The alias.
        self.alias = alias
        # The execution priority.
        self.execute_priority = execute_priority
        # The execution stage.
        self.execute_stage = execute_stage
        # The name of the plug-in.
        self.name = name
        # The plug-in type ID.
        self.plugin_class_id = plugin_class_id
        # The source of the plug-in.
        self.source = source
        # The version.
        self.version = version
        # The description of the version.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority

        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage

        if self.name is not None:
            result['name'] = self.name

        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id

        if self.source is not None:
            result['source'] = self.source

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')

        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        return self

class ListPluginsResponseBodyDataItemsGatewayInfo(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
    ):
        # The instance ID.
        self.gateway_id = gateway_id
        # The instance name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListPluginsResponseBodyDataItemsAttachmentInfo(DaraModel):
    def __init__(
        self,
        enable: str = None,
        plugin_attachment_id: str = None,
    ):
        # Indicates if enabled.
        self.enable = enable
        # The attachment ID.
        self.plugin_attachment_id = plugin_attachment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.plugin_attachment_id is not None:
            result['pluginAttachmentId'] = self.plugin_attachment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('pluginAttachmentId') is not None:
            self.plugin_attachment_id = m.get('pluginAttachmentId')

        return self

