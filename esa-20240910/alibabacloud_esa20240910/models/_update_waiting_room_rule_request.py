# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWaitingRoomRuleRequest(DaraModel):
    def __init__(
        self,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        site_id: int = None,
        waiting_room_rule_id: int = None,
    ):
        # The rule content. A conditional expression is used to match user requests. This parameter is not required when you add a global configuration. Two scenarios are supported:
        # - Match all incoming requests: set the value to true.
        # - Match specified requests: set the value to a custom expression, for example, (http.host eq \\"video.example.com\\").
        # 
        # For the complete syntax of rule expressions, refer to
        # <props="china">https://www.alibabacloud.com/help/en/edge-security-acceleration/esa/user-guide/work-with-rules-engine/
        # <props="intl">https://www.alibabacloud.com/help/edge-security-acceleration/esa/user-guide/work-with-rules-engine/
        # 
        # This parameter is required.
        self.rule = rule
        # Specifies whether to enable the rule. This parameter is not required when you add a global configuration. Valid values:
        # - on: enabled.
        # - off: disabled.
        # 
        # This parameter is required.
        self.rule_enable = rule_enable
        # The rule name. This parameter is not required when you add a global configuration.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The ID of the waiting room bypass rule to update. You can obtain this ID after creating a rule by calling CreateWaitingRoomRule, or by calling the [ListWaitingRoomRules](https://help.aliyun.com/document_detail/2850279.html) operation.
        # 
        # This parameter is required.
        self.waiting_room_rule_id = waiting_room_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.waiting_room_rule_id is not None:
            result['WaitingRoomRuleId'] = self.waiting_room_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('WaitingRoomRuleId') is not None:
            self.waiting_room_rule_id = m.get('WaitingRoomRuleId')

        return self

