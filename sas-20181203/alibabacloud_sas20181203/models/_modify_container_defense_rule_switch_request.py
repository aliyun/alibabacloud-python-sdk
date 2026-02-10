# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyContainerDefenseRuleSwitchRequest(DaraModel):
    def __init__(
        self,
        rule_ids: List[int] = None,
        rule_switch: int = None,
    ):
        # The IDs of the rules.
        self.rule_ids = rule_ids
        # The status of the rule. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.rule_switch = rule_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')

        return self

