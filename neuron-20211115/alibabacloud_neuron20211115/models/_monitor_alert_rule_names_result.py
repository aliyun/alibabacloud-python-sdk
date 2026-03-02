# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MonitorAlertRuleNamesResult(DaraModel):
    def __init__(
        self,
        rule_names: List[str] = None,
    ):
        self.rule_names = rule_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_names is not None:
            result['ruleNames'] = self.rule_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleNames') is not None:
            self.rule_names = m.get('ruleNames')

        return self

