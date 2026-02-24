# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartAggregateRemediationRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        resource_account_id: int = None,
    ):
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # This parameter is required.
        self.config_rule_id = config_rule_id
        self.resource_account_id = resource_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        return self

