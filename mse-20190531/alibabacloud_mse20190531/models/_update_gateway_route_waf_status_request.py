# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayRouteWafStatusRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        enable_waf: bool = None,
        gateway_unique_id: str = None,
        route_id: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # Specifies whether to activate Web Application Firewall (WAF).
        self.enable_waf = enable_waf
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the route.
        self.route_id = route_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.route_id is not None:
            result['RouteId'] = self.route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        return self

