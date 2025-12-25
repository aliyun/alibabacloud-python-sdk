# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_groups: List[main_models.DescribeRuleGroupsResponseBodyRuleGroups] = None,
        total_count: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array of regular expression rule groups.
        self.rule_groups = rule_groups
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.rule_groups:
            for v1 in self.rule_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleGroups'] = []
        if self.rule_groups is not None:
            for k1 in self.rule_groups:
                result['RuleGroups'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_groups = []
        if m.get('RuleGroups') is not None:
            for k1 in m.get('RuleGroups'):
                temp_model = main_models.DescribeRuleGroupsResponseBodyRuleGroups()
                self.rule_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRuleGroupsResponseBodyRuleGroups(DaraModel):
    def __init__(
        self,
        gmt_modified: int = None,
        is_subscribe: int = None,
        parent_rule_group_id: int = None,
        rule_group_id: int = None,
        rule_group_name: str = None,
        rule_total_count: int = None,
    ):
        # The most recent time when the rule group was modified.
        self.gmt_modified = gmt_modified
        # Indicates whether the automatic update feature is enabled for the rule group.
        # 
        # *   1: The automatic update feature is enabled for the rule group.
        # *   2: The automatic update feature is disabled for the rule group.
        self.is_subscribe = is_subscribe
        # The ID of the rule group.
        # 
        # *   0: The rule group is created from scratch.
        # *   1011: The rule group is a strict rule group.
        # *   1012: The rule group is a medium rule group.
        # *   1013: The rue group is a loose rule group.
        self.parent_rule_group_id = parent_rule_group_id
        # The ID of the regular expression rule group.
        self.rule_group_id = rule_group_id
        # The name of the rule group.
        self.rule_group_name = rule_group_name
        # The number of built-in rules in the rule group.
        self.rule_total_count = rule_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.is_subscribe is not None:
            result['IsSubscribe'] = self.is_subscribe

        if self.parent_rule_group_id is not None:
            result['ParentRuleGroupId'] = self.parent_rule_group_id

        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id

        if self.rule_group_name is not None:
            result['RuleGroupName'] = self.rule_group_name

        if self.rule_total_count is not None:
            result['RuleTotalCount'] = self.rule_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IsSubscribe') is not None:
            self.is_subscribe = m.get('IsSubscribe')

        if m.get('ParentRuleGroupId') is not None:
            self.parent_rule_group_id = m.get('ParentRuleGroupId')

        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')

        if m.get('RuleGroupName') is not None:
            self.rule_group_name = m.get('RuleGroupName')

        if m.get('RuleTotalCount') is not None:
            self.rule_total_count = m.get('RuleTotalCount')

        return self

