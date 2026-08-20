# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HttpApiPolicyReference(DaraModel):
    def __init__(
        self,
        policy_attachment_id: str = None,
        policy_id: str = None,
    ):
        # The policy attachment ID.
        self.policy_attachment_id = policy_attachment_id
        # The policy ID.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_attachment_id is not None:
            result['policyAttachmentId'] = self.policy_attachment_id

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyAttachmentId') is not None:
            self.policy_attachment_id = m.get('policyAttachmentId')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        return self

