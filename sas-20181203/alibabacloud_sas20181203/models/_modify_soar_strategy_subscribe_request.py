# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySoarStrategySubscribeRequest(DaraModel):
    def __init__(
        self,
        strategy_id: int = None,
        subscribe_status: bool = None,
    ):
        # The ID of the policy.
        # 
        # >  You can call the [DescribeSoarStrategies](~~DescribeSoarStrategies~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.strategy_id = strategy_id
        # Specifies whether to create the policy template. Valid values:
        # 
        # *   true: creates the policy template
        # *   false: deletes the policy template
        # 
        # This parameter is required.
        self.subscribe_status = subscribe_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.subscribe_status is not None:
            result['SubscribeStatus'] = self.subscribe_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('SubscribeStatus') is not None:
            self.subscribe_status = m.get('SubscribeStatus')

        return self

