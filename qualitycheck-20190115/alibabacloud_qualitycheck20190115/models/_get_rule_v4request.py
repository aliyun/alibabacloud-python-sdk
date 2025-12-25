# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRuleV4Request(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

