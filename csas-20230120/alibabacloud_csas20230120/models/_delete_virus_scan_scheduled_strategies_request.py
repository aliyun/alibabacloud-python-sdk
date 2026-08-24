# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteVirusScanScheduledStrategiesRequest(DaraModel):
    def __init__(
        self,
        strategy_ids: List[str] = None,
    ):
        # The IDs of the virus scheduled scan policies to delete. The collection must contain at least 1 and at most 100 IDs. Duplicate IDs are not allowed.
        # 
        # This parameter is required.
        self.strategy_ids = strategy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strategy_ids is not None:
            result['StrategyIds'] = self.strategy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyIds') is not None:
            self.strategy_ids = m.get('StrategyIds')

        return self

