# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateSwitchStatusRequest(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
        status: str = None,
    ):
        # The ID of the rule.
        # 
        # >  You can call the ListContainerWebDefenseRule operation to query the IDs of rules.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The status of the rule. Valid values: on and off.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

