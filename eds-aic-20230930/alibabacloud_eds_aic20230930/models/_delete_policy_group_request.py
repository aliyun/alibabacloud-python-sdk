# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeletePolicyGroupRequest(DaraModel):
    def __init__(
        self,
        policy_group_ids: List[str] = None,
    ):
        # The IDs of the policies.
        # 
        # This parameter is required.
        self.policy_group_ids = policy_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')

        return self

