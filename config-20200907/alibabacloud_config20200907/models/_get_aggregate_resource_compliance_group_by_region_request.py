# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAggregateResourceComplianceGroupByRegionRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_ids: str = None,
    ):
        # The ID of the account group.
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The rule IDs. Separate multiple rule IDs with commas (,).
        self.config_rule_ids = config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')

        return self

