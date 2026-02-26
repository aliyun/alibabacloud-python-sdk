# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LimitRule(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        condcase: str = None,
        end_time: int = None,
        limit_num: int = None,
        rule_type: str = None,
    ):
        self.begin_time = begin_time
        self.condcase = condcase
        self.end_time = end_time
        self.limit_num = limit_num
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.condcase is not None:
            result['condcase'] = self.condcase

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.limit_num is not None:
            result['limitNum'] = self.limit_num

        if self.rule_type is not None:
            result['ruleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('condcase') is not None:
            self.condcase = m.get('condcase')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('limitNum') is not None:
            self.limit_num = m.get('limitNum')

        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')

        return self

