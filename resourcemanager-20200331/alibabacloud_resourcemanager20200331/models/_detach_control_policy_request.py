# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachControlPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_id: str = None,
        target_id: str = None,
    ):
        # The ID of the control policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The ID of the target node. Valid values:
        # 
        # - Root ID: detaches the control policy from the Root resource folder.
        # - Resource folder ID: detaches the control policy from a resource folder.
        # - Member ID: detaches the control policy from a member.
        # 
        # This parameter is required.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

