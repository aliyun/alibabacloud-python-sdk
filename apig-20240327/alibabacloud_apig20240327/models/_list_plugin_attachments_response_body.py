# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListPluginAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListPluginAttachmentsResponseBodyData = None,
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
            temp_model = main_models.ListPluginAttachmentsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListPluginAttachmentsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListPluginAttachmentsResponseBodyDataItems] = None,
        page_number: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The details of resource attachments.
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
                temp_model = main_models.ListPluginAttachmentsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')

        return self

class ListPluginAttachmentsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        attach_resource_type: str = None,
        enable: bool = None,
        environment_info: main_models.EnvironmentInfo = None,
        parent_resource_info: main_models.ParentResourceInfo = None,
        plugin_attachment_id: str = None,
        plugin_class_info: main_models.PluginClassInfo = None,
        plugin_config: str = None,
        plugin_id: str = None,
        resource_infos: List[main_models.ResourceInfo] = None,
    ):
        # The types of resource attachments.
        # - HttpApi
        # - Operation
        # - GatewayRoute
        # - GatewayDomain
        # - Gateway
        self.attach_resource_type = attach_resource_type
        # Indicates if enabled.
        self.enable = enable
        # The environment metadata.
        self.environment_info = environment_info
        # The parent resource metadata.
        self.parent_resource_info = parent_resource_info
        # The ID of the resource attachment.
        self.plugin_attachment_id = plugin_attachment_id
        # The plug-in type metadata.
        self.plugin_class_info = plugin_class_info
        # The plug-in configurations (Base64-encoded).
        self.plugin_config = plugin_config
        # The plug-in ID.
        self.plugin_id = plugin_id
        # The information of resource attachments.
        self.resource_infos = resource_infos

    def validate(self):
        if self.environment_info:
            self.environment_info.validate()
        if self.parent_resource_info:
            self.parent_resource_info.validate()
        if self.plugin_class_info:
            self.plugin_class_info.validate()
        if self.resource_infos:
            for v1 in self.resource_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.enable is not None:
            result['enable'] = self.enable

        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.parent_resource_info is not None:
            result['parentResourceInfo'] = self.parent_resource_info.to_map()

        if self.plugin_attachment_id is not None:
            result['pluginAttachmentId'] = self.plugin_attachment_id

        if self.plugin_class_info is not None:
            result['pluginClassInfo'] = self.plugin_class_info.to_map()

        if self.plugin_config is not None:
            result['pluginConfig'] = self.plugin_config

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        result['resourceInfos'] = []
        if self.resource_infos is not None:
            for k1 in self.resource_infos:
                result['resourceInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('environmentInfo') is not None:
            temp_model = main_models.EnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('parentResourceInfo') is not None:
            temp_model = main_models.ParentResourceInfo()
            self.parent_resource_info = temp_model.from_map(m.get('parentResourceInfo'))

        if m.get('pluginAttachmentId') is not None:
            self.plugin_attachment_id = m.get('pluginAttachmentId')

        if m.get('pluginClassInfo') is not None:
            temp_model = main_models.PluginClassInfo()
            self.plugin_class_info = temp_model.from_map(m.get('pluginClassInfo'))

        if m.get('pluginConfig') is not None:
            self.plugin_config = m.get('pluginConfig')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        self.resource_infos = []
        if m.get('resourceInfos') is not None:
            for k1 in m.get('resourceInfos'):
                temp_model = main_models.ResourceInfo()
                self.resource_infos.append(temp_model.from_map(k1))

        return self

