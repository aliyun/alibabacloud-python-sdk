# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEmptyNumberNoMoreCallsInfoRequest(DaraModel):
    def __init__(
        self,
        empty_number_no_more_calls: bool = None,
        entry_id: str = None,
        strategy_level: int = None,
    ):
        self.empty_number_no_more_calls = empty_number_no_more_calls
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
        if self.empty_number_no_more_calls is not None:
            result['EmptyNumberNoMoreCalls'] = self.empty_number_no_more_calls

        if self.entry_id is not None:
            result['EntryId'] = self.entry_id

        if self.strategy_level is not None:
            result['StrategyLevel'] = self.strategy_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmptyNumberNoMoreCalls') is not None:
            self.empty_number_no_more_calls = m.get('EmptyNumberNoMoreCalls')

        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')

        if m.get('StrategyLevel') is not None:
            self.strategy_level = m.get('StrategyLevel')

        return self

