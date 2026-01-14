# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdatePluginConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        config: str = None,
        config_level: int = None,
        enable: bool = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        plugin_id: int = None,
        resource_id_list: List[int] = None,
    ):
        # The language of the response. Valid values:
        # 
        # zh: Chinese en: English
        self.accept_language = accept_language
        self.config = config
        # The application scope of the plug-in.
        # 
        # *   0: global
        # *   1: route
        # *   2: domain name
        self.config_level = config_level
        # Specifies whether to enable the plug-in.
        self.enable = enable
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The ID of the plug-in configuration.
        self.id = id
        # The ID of the gateway plug-in.
        self.plugin_id = plugin_id
        self.resource_id_list = resource_id_list

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

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.resource_id_list is not None:
            result['ResourceIdList'] = self.resource_id_list

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

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('ResourceIdList') is not None:
            self.resource_id_list = m.get('ResourceIdList')

        return self

