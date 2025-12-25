# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class Attachment(DaraModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        attach_resource_type: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        policy_attachment_id: str = None,
    ):
        self.attach_resource_ids = attach_resource_ids
        self.attach_resource_type = attach_resource_type
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.policy_attachment_id = policy_attachment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids

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
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('policyAttachmentId') is not None:
            self.policy_attachment_id = m.get('policyAttachmentId')

        return self

