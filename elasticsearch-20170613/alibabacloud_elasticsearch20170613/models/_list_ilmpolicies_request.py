# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListILMPoliciesRequest(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        return self

