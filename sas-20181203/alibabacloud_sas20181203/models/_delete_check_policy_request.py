# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteCheckPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_ids: List[int] = None,
        policy_type: str = None,
    ):
        # Array of policies to delete
        # 
        # This parameter is required.
        self.policy_ids = policy_ids
        # Policy type for custom check rule:
        # 
        # *   **STANDARD**: Standard-level policy
        # *   **REQUIREMENT**: Requirement-level policy
        # *   **SECTION**: Section-level policy
        # 
        # This parameter is required.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

