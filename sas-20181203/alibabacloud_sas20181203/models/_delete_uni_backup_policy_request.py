# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUniBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_id: int = None,
        policy_ids: str = None,
    ):
        # The ID of the anti-ransomware policy.
        # 
        # >  You can call the [DescribeUniBackupPolicies](~~DescribeUniBackupPolicies~~) operation to query the IDs of anti-ransomware policies. You must specify at least one of the PolicyId parameter and the **PolicyIds** parameter.
        self.policy_id = policy_id
        # The IDs of anti-ransomware policies.
        # 
        # >  You can call the [DescribeUniBackupPolicies](~~DescribeUniBackupPolicies~~) operation to query the IDs of anti-ransomware policies. You must specify at least one of the **PolicyId** parameter and the PolicyIds parameter.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        return self

