# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class Attachment(DaraModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_ids: List[str] = None,
        attach_resource_parent_ids: List[str] = None,
        attach_resource_type: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        policy_attachment_id: str = None,
    ):
        # The attachment point ID.
        self.attach_resource_id = attach_resource_id
        # A list of attached resource IDs.
        self.attach_resource_ids = attach_resource_ids
        # A list of parent resource IDs.
        self.attach_resource_parent_ids = attach_resource_parent_ids
        # The supported attachment point types for the policy.
        # 
        # - `HttpApi`: An HTTP API.
        # 
        # - `Operation`: An operation of an HTTP API.
        # 
        # - `GatewayRoute`: A gateway route.
        # 
        # - `GatewayService`: A gateway service.
        # 
        # - `GatewayServicePort`: A gateway service port.
        # 
        # - `Domain`: A gateway domain.
        # 
        # - `Gateway`: A gateway.
        self.attach_resource_type = attach_resource_type
        # The ID of the environment for the attached resource. An asterisk (`*`) indicates that the policy attachment is not environment-specific.
        self.environment_id = environment_id
        # The ID of the gateway for the attached resource.
        self.gateway_id = gateway_id
        # The policy attachment ID.
        self.policy_attachment_id = policy_attachment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_id is not None:
            result['attachResourceId'] = self.attach_resource_id

        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids

        if self.attach_resource_parent_ids is not None:
            result['attachResourceParentIds'] = self.attach_resource_parent_ids

        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.policy_attachment_id is not None:
            result['policyAttachmentId'] = self.policy_attachment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')

        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')

        if m.get('attachResourceParentIds') is not None:
            self.attach_resource_parent_ids = m.get('attachResourceParentIds')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('policyAttachmentId') is not None:
            self.policy_attachment_id = m.get('policyAttachmentId')

        return self

