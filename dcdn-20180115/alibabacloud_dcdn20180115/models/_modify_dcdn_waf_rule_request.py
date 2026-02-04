# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDcdnWafRuleRequest(DaraModel):
    def __init__(
        self,
        rule_config: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_status: str = None,
    ):
        # The new configurations of the protection rule.
        # 
        # > After you modify the configurations of the protection rule, the previous configurations are overwritten.
        self.rule_config = rule_config
        # The ID of the protection rule. You can specify only one ID in each request.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The new name of the protection rule.
        self.rule_name = rule_name
        # The new status of the protection rule. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        return self

