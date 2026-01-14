# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePluginConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        config: str = None,
        config_level: int = None,
        enable: bool = None,
        gateway_unique_id: str = None,
        plugin_id: int = None,
        resource_id_list_shrink: str = None,
    ):
        # The language in which you want to display the results. Valid values: zh and en. zh indicates Chinese, which is the default value. en indicates English.
        self.accept_language = accept_language
        self.config = config
        # The application scope of the plug-in. Valid values:
        # 
        # *   0: global
        # *   1: route
        # *   2: domain name
        # 
        # This parameter is required.
        self.config_level = config_level
        # Indicates whether the plug-in is enabled.
        # 
        # This parameter is required.
        self.enable = enable
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The gateway plug-in ID.
        # 
        # This parameter is required.
        self.plugin_id = plugin_id
        # The domain IDs or route IDs. They are distinguished based on ConfigLevel.
        self.resource_id_list_shrink = resource_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.config is not None:
            result['Config'] = self.config

        if self.config_level is not None:
            result['ConfigLevel'] = self.config_level

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.resource_id_list_shrink is not None:
            result['ResourceIdList'] = self.resource_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigLevel') is not None:
            self.config_level = m.get('ConfigLevel')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('ResourceIdList') is not None:
            self.resource_id_list_shrink = m.get('ResourceIdList')

        return self

