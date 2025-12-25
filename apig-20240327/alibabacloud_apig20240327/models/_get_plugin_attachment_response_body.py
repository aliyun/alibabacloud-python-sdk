# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetPluginAttachmentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPluginAttachmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response payload.
        self.data = data
        # The status message.
        self.message = message
        # The ID of the request.
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
            temp_model = main_models.GetPluginAttachmentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPluginAttachmentResponseBodyData(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        environment_info: main_models.EnvironmentInfo = None,
        gateway_info: main_models.GatewayInfo = None,
        parent_resource_info: main_models.ParentResourceInfo = None,
        plugin_attachment_id: str = None,
        plugin_class_info: main_models.PluginClassInfo = None,
        plugin_config: str = None,
        plugin_id: str = None,
        resource_infos: List[main_models.ResourceInfo] = None,
    ):
        # Indicates whether the plug-in is enabled.
        self.enable = enable
        # The environment information.
        self.environment_info = environment_info
        # The instance information.
        self.gateway_info = gateway_info
        # The information about the parent resource to which the plug-in is attached.
        self.parent_resource_info = parent_resource_info
        # The attachment ID.
        self.plugin_attachment_id = plugin_attachment_id
        # The plug-in type information.
        self.plugin_class_info = plugin_class_info
        # The Base64-encoded configurations of the plug-in.
        self.plugin_config = plugin_config
        # The plug-in ID.
        self.plugin_id = plugin_id
        # The resource details.
        self.resource_infos = resource_infos

    def validate(self):
        if self.environment_info:
            self.environment_info.validate()
        if self.gateway_info:
            self.gateway_info.validate()
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
        if self.enable is not None:
            result['enable'] = self.enable

        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

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
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('environmentInfo') is not None:
            temp_model = main_models.EnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

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

