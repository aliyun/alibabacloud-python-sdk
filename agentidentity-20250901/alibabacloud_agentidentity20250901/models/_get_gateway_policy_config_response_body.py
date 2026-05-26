# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetGatewayPolicyConfigResponseBody(DaraModel):
    def __init__(
        self,
        gateway_policy_config: main_models.GetGatewayPolicyConfigResponseBodyGatewayPolicyConfig = None,
        request_id: str = None,
    ):
        self.gateway_policy_config = gateway_policy_config
        self.request_id = request_id

    def validate(self):
        if self.gateway_policy_config:
            self.gateway_policy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_policy_config is not None:
            result['GatewayPolicyConfig'] = self.gateway_policy_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayPolicyConfig') is not None:
            temp_model = main_models.GetGatewayPolicyConfigResponseBodyGatewayPolicyConfig()
            self.gateway_policy_config = temp_model.from_map(m.get('GatewayPolicyConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetGatewayPolicyConfigResponseBodyGatewayPolicyConfig(DaraModel):
    def __init__(
        self,
        enforcement_mode: str = None,
        policy_set_arn: str = None,
    ):
        self.enforcement_mode = enforcement_mode
        self.policy_set_arn = policy_set_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enforcement_mode is not None:
            result['EnforcementMode'] = self.enforcement_mode

        if self.policy_set_arn is not None:
            result['PolicySetArn'] = self.policy_set_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnforcementMode') is not None:
            self.enforcement_mode = m.get('EnforcementMode')

        if m.get('PolicySetArn') is not None:
            self.policy_set_arn = m.get('PolicySetArn')

        return self

