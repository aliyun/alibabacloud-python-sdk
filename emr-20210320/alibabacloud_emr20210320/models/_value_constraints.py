# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ValueConstraints(DaraModel):
    def __init__(
        self,
        default_value: int = None,
        end: int = None,
        start: int = None,
        step: int = None,
        type: str = None,
        values: List[int] = None,
    ):
        # 默认值。
        self.default_value = default_value
        # 结束值。
        self.end = end
        # 起始值。
        self.start = start
        # 步长。
        self.step = step
        # 值限制类型。
        self.type = type
        # 枚举值。
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        if self.step is not None:
            result['Step'] = self.step

        if self.type is not None:
            result['Type'] = self.type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

