# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayPolicyConfigRequest(DaraModel):
    def __init__(
        self,
        enforcement_mode: str = None,
        gateway_arn: str = None,
        gateway_type: str = None,
    ):
        self.enforcement_mode = enforcement_mode
        self.gateway_arn = gateway_arn
        self.gateway_type = gateway_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enforcement_mode is not None:
            result['EnforcementMode'] = self.enforcement_mode

        if self.gateway_arn is not None:
            result['GatewayArn'] = self.gateway_arn

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnforcementMode') is not None:
            self.enforcement_mode = m.get('EnforcementMode')

        if m.get('GatewayArn') is not None:
            self.gateway_arn = m.get('GatewayArn')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        return self

