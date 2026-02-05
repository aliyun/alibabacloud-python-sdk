# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveEffectiveDaysRequest(DaraModel):
    def __init__(
        self,
        effective_days: int = None,
        entry_id: str = None,
        strategy_level: int = None,
    ):
        self.effective_days = effective_days
        # This parameter is required.
        self.entry_id = entry_id
        self.strategy_level = strategy_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_days is not None:
            result['EffectiveDays'] = self.effective_days

        if self.entry_id is not None:
            result['EntryId'] = self.entry_id

        if self.strategy_level is not None:
            result['StrategyLevel'] = self.strategy_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveDays') is not None:
            self.effective_days = m.get('EffectiveDays')

        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')

        if m.get('StrategyLevel') is not None:
            self.strategy_level = m.get('StrategyLevel')

        return self

