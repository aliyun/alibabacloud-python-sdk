# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribePoliciesV2Request(DaraModel):
    def __init__(
        self,
        account_scope: str = None,
        accounts: List[main_models.DescribePoliciesV2RequestAccounts] = None,
        max_results: int = None,
        next_token: str = None,
        policy_id: str = None,
        rule_scope: str = None,
    ):
        self.account_scope = account_scope
        self.accounts = accounts
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
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_scope is not None:
            result['AccountScope'] = self.account_scope

        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

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

        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.DescribePoliciesV2RequestAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RuleScope') is not None:
            self.rule_scope = m.get('RuleScope')

        return self

class DescribePoliciesV2RequestAccounts(DaraModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
    ):
        self.cross_account_role_name = cross_account_role_name
        self.cross_account_type = cross_account_type
        self.cross_account_user_id = cross_account_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        return self

