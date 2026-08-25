# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePoliciesV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        account_scope: str = None,
        accounts_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        policy_id: str = None,
        rule_scope: str = None,
    ):
        self.account_scope = account_scope
        self.accounts_shrink = accounts_shrink
        # The number of results per query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The token required to retrieve the next page of policies.
        self.next_token = next_token
        # The policy ID.
        self.policy_id = policy_id
        self.rule_scope = rule_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_scope is not None:
            result['AccountScope'] = self.account_scope

        if self.accounts_shrink is not None:
            result['Accounts'] = self.accounts_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.rule_scope is not None:
            result['RuleScope'] = self.rule_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScope') is not None:
            self.account_scope = m.get('AccountScope')

        if m.get('Accounts') is not None:
            self.accounts_shrink = m.get('Accounts')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RuleScope') is not None:
            self.rule_scope = m.get('RuleScope')

        return self

