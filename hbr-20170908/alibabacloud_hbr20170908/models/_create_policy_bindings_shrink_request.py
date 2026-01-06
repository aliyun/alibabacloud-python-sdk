# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyBindingsShrinkRequest(DaraModel):
    def __init__(
        self,
        policy_binding_list_shrink: str = None,
        policy_id: str = None,
    ):
        # The data sources that you want to bind to the backup policy.
        self.policy_binding_list_shrink = policy_binding_list_shrink
        # The ID of the backup policy.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_binding_list_shrink is not None:
            result['PolicyBindingList'] = self.policy_binding_list_shrink

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyBindingList') is not None:
            self.policy_binding_list_shrink = m.get('PolicyBindingList')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

