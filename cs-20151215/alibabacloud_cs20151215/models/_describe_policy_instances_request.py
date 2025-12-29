# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolicyInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        policy_name: str = None,
    ):
        # The name of the policy instance that you want to query.
        self.instance_name = instance_name
        # The name of the policy that you want to query.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name

        if self.policy_name is not None:
            result['policy_name'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')

        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')

        return self

