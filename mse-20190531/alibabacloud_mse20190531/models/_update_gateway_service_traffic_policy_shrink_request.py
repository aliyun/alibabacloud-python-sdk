# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayServiceTrafficPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_traffic_policy_shrink: str = None,
        gateway_unique_id: str = None,
        service_id: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   **zh-CN** (default): Chinese
        # *   **en-US**: English
        self.accept_language = accept_language
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The traffic policy of the gateway.
        # 
        # This parameter is required.
        self.gateway_traffic_policy_shrink = gateway_traffic_policy_shrink
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the service.
        self.service_id = service_id

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

        if self.gateway_traffic_policy_shrink is not None:
            result['GatewayTrafficPolicy'] = self.gateway_traffic_policy_shrink

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayTrafficPolicy') is not None:
            self.gateway_traffic_policy_shrink = m.get('GatewayTrafficPolicy')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        return self

