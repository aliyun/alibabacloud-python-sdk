# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAggregateRemediationExecutionsRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        execution_status: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_account_id: int = None,
    ):
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # This parameter is required.
        self.config_rule_id = config_rule_id
        self.execution_status = execution_status
        self.max_results = max_results
        self.next_token = next_token
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

        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        return self

