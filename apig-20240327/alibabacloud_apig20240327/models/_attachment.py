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
        # attachResourceId
        self.attach_resource_id = attach_resource_id
        # The list of mounted resource IDs.
        self.attach_resource_ids = attach_resource_ids
        # The list of parent IDs of the mounted resource.
        self.attach_resource_parent_ids = attach_resource_parent_ids
        # The type of mount point supported by the policy. Valid values:
        # 
        # - HttpApi: HttpApi.
        # - Operation: Operation of HttpApi.
        # - GatewayRoute: gateway route.
        # - GatewayService: gateway service.
        # - GatewayServicePort: gateway service port.
        # - Domain: gateway domain name.
        # - Gateway: gateway.
        self.attach_resource_type = attach_resource_type
        # The environment to which the mounted resource belongs. If the environment ID is *, the mounted resource of the policy is not associated with any environment.
        self.environment_id = environment_id
        # The gateway to which the mounted resource belongs.
        self.gateway_id = gateway_id
        # The policy mount ID.
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

