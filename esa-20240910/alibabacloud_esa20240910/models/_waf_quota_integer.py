# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WafQuotaInteger(DaraModel):
    def __init__(
        self,
        equal: int = None,
        greater_than: int = None,
        greater_than_or_equal: int = None,
        less_than: int = None,
        less_than_or_equal: int = None,
    ):
        self.equal = equal
        self.greater_than = greater_than
        self.greater_than_or_equal = greater_than_or_equal
        self.less_than = less_than
        self.less_than_or_equal = less_than_or_equal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.equal is not None:
            result['Equal'] = self.equal

        if self.greater_than is not None:
            result['GreaterThan'] = self.greater_than

        if self.greater_than_or_equal is not None:
            result['GreaterThanOrEqual'] = self.greater_than_or_equal

        if self.less_than is not None:
            result['LessThan'] = self.less_than

        if self.less_than_or_equal is not None:
            result['LessThanOrEqual'] = self.less_than_or_equal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Equal') is not None:
            self.equal = m.get('Equal')

        if m.get('GreaterThan') is not None:
            self.greater_than = m.get('GreaterThan')

        if m.get('GreaterThanOrEqual') is not None:
            self.greater_than_or_equal = m.get('GreaterThanOrEqual')

        if m.get('LessThan') is not None:
            self.less_than = m.get('LessThan')

        if m.get('LessThanOrEqual') is not None:
            self.less_than_or_equal = m.get('LessThanOrEqual')

        return self

