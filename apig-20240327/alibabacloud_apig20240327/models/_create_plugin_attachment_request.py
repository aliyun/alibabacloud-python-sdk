# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreatePluginAttachmentRequest(DaraModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        attach_resource_type: str = None,
        enable: bool = None,
        environment_id: str = None,
        gateway_id: str = None,
        plugin_config: str = None,
        plugin_id: str = None,
    ):
        # The attachment IDs.
        self.attach_resource_ids = attach_resource_ids
        # The type of the resource to which the plug-in is attached. Valid values: GatewayRoute, Gateway, GatewayDomain, HttpApi, and Operation.
        self.attach_resource_type = attach_resource_type
        # Specifies whether to enable the plug-in. Default value: false.
        self.enable = enable
        # The environment ID.
        self.environment_id = environment_id
        # The instance ID.
        self.gateway_id = gateway_id
        # The Base64-encoded configurations of the plug-in.
        self.plugin_config = plugin_config
        # The plug-in ID.
        self.plugin_id = plugin_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids

        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.enable is not None:
            result['enable'] = self.enable

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.plugin_config is not None:
            result['pluginConfig'] = self.plugin_config

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('pluginConfig') is not None:
            self.plugin_config = m.get('pluginConfig')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        return self

