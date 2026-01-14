# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPluginsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        category: int = None,
        enable_only: bool = None,
        gateway_unique_id: str = None,
        name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # zh: Chinese en: English
        self.accept_language = accept_language
        # The type of the plug-in. Valid values:
        # 
        # *   0: custom
        # *   1: permission authorization
        # *   2: security protection
        # *   3: transmission protocol
        # *   4: traffic control
        # *   5: traffic observation
        self.category = category
        # Specifies whether to enable the plug-in.
        self.enable_only = enable_only
        # The ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The name of the plug-in.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.category is not None:
            result['Category'] = self.category

        if self.enable_only is not None:
            result['EnableOnly'] = self.enable_only

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('EnableOnly') is not None:
            self.enable_only = m.get('EnableOnly')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

