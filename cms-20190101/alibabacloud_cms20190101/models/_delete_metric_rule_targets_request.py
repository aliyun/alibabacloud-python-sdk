# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteMetricRuleTargetsRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        rule_id: str = None,
        target_ids: List[str] = None,
    ):
        self.region_id = region_id
        # The ID of the alert rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The resource IDs.
        # 
        # This parameter is required.
        self.target_ids = target_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')

        return self

