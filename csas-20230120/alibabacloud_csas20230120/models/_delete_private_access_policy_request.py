# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePrivateAccessPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # The ID of the private network access policy. Obtain this ID from:
        # 
        # - [ListPrivateAccessPolices](~~ListPrivateAccessPolices~~): Batch query private network access policies.
        # 
        # - [CreatePrivateAccessPolicy](~~CreatePrivateAccessPolicy~~): Create a private network access policy.
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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

