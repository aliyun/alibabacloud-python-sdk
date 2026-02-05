# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveMaxAttemptsPerDayRequest(DaraModel):
    def __init__(
        self,
        entry_id: str = None,
        max_attempts_per_day: int = None,
        strategy_level: int = None,
    ):
        # This parameter is required.
        self.entry_id = entry_id
        self.max_attempts_per_day = max_attempts_per_day
        self.strategy_level = strategy_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id

        if self.max_attempts_per_day is not None:
            result['MaxAttemptsPerDay'] = self.max_attempts_per_day

        if self.strategy_level is not None:
            result['StrategyLevel'] = self.strategy_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')

        if m.get('MaxAttemptsPerDay') is not None:
            self.max_attempts_per_day = m.get('MaxAttemptsPerDay')

        if m.get('StrategyLevel') is not None:
            self.strategy_level = m.get('StrategyLevel')

        return self

