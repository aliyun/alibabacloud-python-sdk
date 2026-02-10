# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAegisContainerPluginRuleResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListAegisContainerPluginRuleResponseBodyPageInfo = None,
        request_id: str = None,
        rule_list: List[main_models.ListAegisContainerPluginRuleResponseBodyRuleList] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # The rules.
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
            temp_model = main_models.ListAegisContainerPluginRuleResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.ListAegisContainerPluginRuleResponseBodyRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        return self

class ListAegisContainerPluginRuleResponseBodyRuleList(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        mode: int = None,
        policies: List[main_models.ListAegisContainerPluginRuleResponseBodyRuleListPolicies] = None,
        rule_description: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_template_id: str = None,
        rule_template_name: str = None,
        selected_policy: List[str] = None,
        switch_id: str = None,
        white_images: List[str] = None,
    ):
        # The time when the rule was created. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The time when the rule was modified. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The action of the rule. Valid values:
        # 
        # *   **1**: Alert
        # *   **2**: Block
        self.mode = mode
        # An array that consists of policies.
        self.policies = policies
        # The description of the rule.
        self.rule_description = rule_description
        # The ID of the rule.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # The ID of the rule template. The ListSystemClientRules operation returns the ID of a rule template.
        self.rule_template_id = rule_template_id
        # The name of the rule template.
        self.rule_template_name = rule_template_name
        # The fields in the value of the rule subtype.
        self.selected_policy = selected_policy
        # The switch ID of the rule.
        self.switch_id = switch_id
        # The images that are added to the whitelist of the rule.
        self.white_images = white_images

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
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.mode is not None:
            result['Mode'] = self.mode

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.rule_description is not None:
            result['RuleDescription'] = self.rule_description

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_template_id is not None:
            result['RuleTemplateId'] = self.rule_template_id

        if self.rule_template_name is not None:
            result['RuleTemplateName'] = self.rule_template_name

        if self.selected_policy is not None:
            result['SelectedPolicy'] = self.selected_policy

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.white_images is not None:
            result['WhiteImages'] = self.white_images

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListAegisContainerPluginRuleResponseBodyRuleListPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RuleDescription') is not None:
            self.rule_description = m.get('RuleDescription')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleTemplateId') is not None:
            self.rule_template_id = m.get('RuleTemplateId')

        if m.get('RuleTemplateName') is not None:
            self.rule_template_name = m.get('RuleTemplateName')

        if m.get('SelectedPolicy') is not None:
            self.selected_policy = m.get('SelectedPolicy')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('WhiteImages') is not None:
            self.white_images = m.get('WhiteImages')

        return self

class ListAegisContainerPluginRuleResponseBodyRuleListPolicies(DaraModel):
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

class ListAegisContainerPluginRuleResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
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

