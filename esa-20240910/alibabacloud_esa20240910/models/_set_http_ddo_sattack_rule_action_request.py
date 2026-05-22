# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetHttpDDoSAttackRuleActionRequest(DaraModel):
    def __init__(
        self,
        rule_action: str = None,
        rule_ids: str = None,
        site_id: int = None,
    ):
        # Rule action, with values:
        # 
        # - **deny**: Block.
        # 
        # - **js**: JS Verification.
        # 
        # - **observe**: Observe.
        # 
        # This parameter is required.
        self.rule_action = rule_action
        # List of rule IDs to be operated on, separated by English commas (,).
        # > You can call the [DescribeHttpDDoSAttackRules](~~DescribeHttpDDoSAttackRules~~) API to get this parameter.
        # 
        # This parameter is required.
        self.rule_ids = rule_ids
        # Site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) API.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

