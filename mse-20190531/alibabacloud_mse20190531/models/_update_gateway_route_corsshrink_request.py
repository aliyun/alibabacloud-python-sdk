# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayRouteCORSShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cors_jsonshrink: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
    ):
        # The language of the response. In compliance with [RFC 7231](https://tools.ietf.org/html/rfc7231), the backend service must return a response based on the language used by the user.
        # 
        # *   No default value.
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language
        # The information about the CORS policy.
        self.cors_jsonshrink = cors_jsonshrink
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the associated record.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cors_jsonshrink is not None:
            result['CorsJSON'] = self.cors_jsonshrink

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('CorsJSON') is not None:
            self.cors_jsonshrink = m.get('CorsJSON')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

