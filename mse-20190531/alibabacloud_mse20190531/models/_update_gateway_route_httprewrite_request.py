# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayRouteHTTPRewriteRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        http_rewrite_json: str = None,
        id: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The information about the rewrite policy. The JSON format is supported.
        self.http_rewrite_json = http_rewrite_json
        # The ID of the route.
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

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.http_rewrite_json is not None:
            result['HttpRewriteJSON'] = self.http_rewrite_json

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('HttpRewriteJSON') is not None:
            self.http_rewrite_json = m.get('HttpRewriteJSON')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

