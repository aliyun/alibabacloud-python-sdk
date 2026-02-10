# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListSystemClientRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListSystemClientRulesResponseBodyPageInfo = None,
        request_id: str = None,
        rule_list: List[main_models.ListSystemClientRulesResponseBodyRuleList] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the system defense rules.
        self.rule_list = rule_list

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListSystemClientRulesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.ListSystemClientRulesResponseBodyRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        return self

class ListSystemClientRulesResponseBodyRuleList(DaraModel):
    def __init__(
        self,
        aggregation_name: str = None,
        description: str = None,
        platform: str = None,
        policies: List[main_models.ListSystemClientRulesResponseBodyRuleListPolicies] = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_type: int = None,
        status: int = None,
        switch_enable: bool = None,
        switch_id: str = None,
    ):
        # The name of the aggregation type for the system defense rule.
        self.aggregation_name = aggregation_name
        # The description of the system defense rule.
        self.description = description
        # The type of the OS. Valid values:
        # 
        # *   **windows**: Windows
        # *   **linux**: Linux
        # *   **all**: all types
        self.platform = platform
        # An array that consists of policies.
        self.policies = policies
        # The ID of the system defense rule.
        self.rule_id = rule_id
        # The name of the system defense rule.
        self.rule_name = rule_name
        # The type of the system defense rule. Valid values:
        # 
        # *   **1**: alihips, process-specific defense
        # *   **2**: alinet, network-specific defense
        self.rule_type = rule_type
        # The status of the system defense rule. Valid values:
        # 
        # *   **online**: enabled
        # *   **offline**: disabled
        self.status = status
        # Whether the current rule switch takes effect. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.switch_enable = switch_enable
        # The switch ID of the system defense rule.
        self.switch_id = switch_id

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_name is not None:
            result['AggregationName'] = self.aggregation_name

        if self.description is not None:
            result['Description'] = self.description

        if self.platform is not None:
            result['Platform'] = self.platform

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_enable is not None:
            result['SwitchEnable'] = self.switch_enable

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationName') is not None:
            self.aggregation_name = m.get('AggregationName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListSystemClientRulesResponseBodyRuleListPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchEnable') is not None:
            self.switch_enable = m.get('SwitchEnable')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        return self

class ListSystemClientRulesResponseBodyRuleListPolicies(DaraModel):
    def __init__(
        self,
        policy_key: str = None,
        policy_name: str = None,
    ):
        # The policy key.
        self.policy_key = policy_key
        # The name of the policy.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_key is not None:
            result['PolicyKey'] = self.policy_key

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyKey') is not None:
            self.policy_key = m.get('PolicyKey')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

class ListSystemClientRulesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

