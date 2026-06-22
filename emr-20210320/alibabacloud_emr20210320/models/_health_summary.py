# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HealthSummary(DaraModel):
    def __init__(
        self,
        bad_count: int = None,
        good_count: int = None,
        none_count: int = None,
        stopped_count: int = None,
        total_count: int = None,
        unknown_count: int = None,
        warning_count: int = None,
    ):
        self.bad_count = bad_count
        self.good_count = good_count
        self.none_count = none_count
        self.stopped_count = stopped_count
        self.total_count = total_count
        self.unknown_count = unknown_count
        self.warning_count = warning_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bad_count is not None:
            result['BadCount'] = self.bad_count

        if self.good_count is not None:
            result['GoodCount'] = self.good_count

        if self.none_count is not None:
            result['NoneCount'] = self.none_count

        if self.stopped_count is not None:
            result['StoppedCount'] = self.stopped_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.unknown_count is not None:
            result['UnknownCount'] = self.unknown_count

        if self.warning_count is not None:
            result['WarningCount'] = self.warning_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BadCount') is not None:
            self.bad_count = m.get('BadCount')

        if m.get('GoodCount') is not None:
            self.good_count = m.get('GoodCount')

        if m.get('NoneCount') is not None:
            self.none_count = m.get('NoneCount')

        if m.get('StoppedCount') is not None:
            self.stopped_count = m.get('StoppedCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UnknownCount') is not None:
            self.unknown_count = m.get('UnknownCount')

        if m.get('WarningCount') is not None:
            self.warning_count = m.get('WarningCount')

        return self

