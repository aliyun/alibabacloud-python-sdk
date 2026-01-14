# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBlackWhiteListRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        is_white: bool = None,
        resource_type: str = None,
        type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # Specifies whether to enable the whitelist.
        self.is_white = is_white
        # The type of the resource.
        self.resource_type = resource_type
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.is_white is not None:
            result['IsWhite'] = self.is_white

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

