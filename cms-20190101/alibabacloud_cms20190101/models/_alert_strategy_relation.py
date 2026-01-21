# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlertStrategyRelation(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        strategy_uuid: str = None,
    ):
        self.alert_name = alert_name
        self.strategy_uuid = strategy_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.strategy_uuid is not None:
            result['StrategyUuid'] = self.strategy_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('StrategyUuid') is not None:
            self.strategy_uuid = m.get('StrategyUuid')

        return self

