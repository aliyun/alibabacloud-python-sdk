# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyAttachmentRequest(DaraModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        policy_id: str = None,
    ):
        # Attached resource ID
        # 
        # This parameter is required.
        self.attach_resource_id = attach_resource_id
        # Attached resource type, such as HttpApi, GatewayRoute, Operation, GatewayService, GatewayServicePort, Gateway, Domain
        # 
        # This parameter is required.
        self.attach_resource_type = attach_resource_type
        # Environment ID
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # Gateway instance ID
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # Policy ID
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_id is not None:
            result['attachResourceId'] = self.attach_resource_id

        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        return self

