# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachPolicySetFromGatewayRequest(DaraModel):
    def __init__(
        self,
        gateway_arn: str = None,
        gateway_type: str = None,
        policy_set_name: str = None,
    ):
        self.gateway_arn = gateway_arn
        self.gateway_type = gateway_type
        self.policy_set_name = policy_set_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_arn is not None:
            result['GatewayArn'] = self.gateway_arn

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.policy_set_name is not None:
            result['PolicySetName'] = self.policy_set_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayArn') is not None:
            self.gateway_arn = m.get('GatewayArn')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('PolicySetName') is not None:
            self.policy_set_name = m.get('PolicySetName')

        return self

