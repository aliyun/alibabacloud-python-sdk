# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClientRuleStrategyStatisticsRequest(DaraModel):
    def __init__(
        self,
        policy_type: int = None,
    ):
        # The policy type. Set this parameter to 2 to query the statistics of proactive defense policies.
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
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

