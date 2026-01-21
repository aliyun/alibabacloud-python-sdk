# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMonitorGroupNotifyPolicyRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        policy_type: str = None,
        region_id: str = None,
    ):
        # The ID of the application group.
        self.group_id = group_id
        # The type of the policy.
        # 
        # Valid value: PauseNotify.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

