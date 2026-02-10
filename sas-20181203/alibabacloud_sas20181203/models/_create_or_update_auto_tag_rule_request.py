# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateAutoTagRuleRequest(DaraModel):
    def __init__(
        self,
        check_all: bool = None,
        expression: str = None,
        rule_desc: str = None,
        rule_id: int = None,
        rule_name: str = None,
        tag_context: str = None,
        tag_type: str = None,
    ):
        # Specifies whether to check the rule on the backend. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.check_all = check_all
        # The expression of the rule.
        self.expression = expression
        # The description of the rule.
        self.rule_desc = rule_desc
        # The ID of the rule.
        # 
        # >  You can call the [ListAutoTagRules](~~ListAutoTagRules~~) operation to query the ID.
        self.rule_id = rule_id
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The tag specified by the operation type of the rule.
        # 
        # *   If TagType is set to group, set this parameter to {"groupId":XXX}. XXX specifies the ID of the group. You can call the [DescribeGroupStruct](~~DescribeGroupStruct~~) operation to query the ID.
        # *   If TagType is set to tag, set this parameter to {"tagId":XXX}. XXX specifies the ID of the tag. You can call the [DescribeGroupedTags](~~DescribeGroupedTags~~) operation to query the ID.
        self.tag_context = tag_context
        # The operation type of the rule. Valid values:
        # 
        # *   **group**
        # *   **tag**
        # 
        # This parameter is required.
        self.tag_type = tag_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_all is not None:
            result['CheckAll'] = self.check_all

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.tag_context is not None:
            result['TagContext'] = self.tag_context

        if self.tag_type is not None:
            result['TagType'] = self.tag_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckAll') is not None:
            self.check_all = m.get('CheckAll')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TagContext') is not None:
            self.tag_context = m.get('TagContext')

        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')

        return self

