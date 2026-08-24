# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVirusScanScheduledStrategyRequest(DaraModel):
    def __init__(
        self,
        strategy_id: str = None,
    ):
        # The ID of the scheduled virus scan policy. You can obtain the value from the following operations:
        # - [ListVirusScanScheduledStrategies](~~ListVirusScanScheduledStrategies~~): Lists scheduled virus scan policies.
        # - [CreateVirusScanScheduledStrategy](~~CreateVirusScanScheduledStrategy~~): Creates a scheduled virus scan policy.
        self.strategy_id = strategy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        return self

