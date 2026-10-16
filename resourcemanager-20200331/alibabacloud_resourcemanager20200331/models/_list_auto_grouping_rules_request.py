# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAutoGroupingRulesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
    ):
        # The maximum number of entries to return in a single request. Valid values: 1 to 50.
        self.max_results = max_results
        # If the response is truncated, you can use NextToken to send another request to retrieve the content after the current truncation point.
        self.next_token = next_token
        # The rule ID.
        self.rule_id = rule_id
        # The rule name.
        self.rule_name = rule_name
        # The rule type. Valid values:
        # - custom_condition: custom rule-based group transfer.
        # - associated_transfer: attached-resource allocation group transfer.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

