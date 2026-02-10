# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSoarStrategyTaskRequest(DaraModel):
    def __init__(
        self,
        strategy_task_id: int = None,
    ):
        # The ID of the policy task that is in the waiting state.
        # 
        # >  You can call the [DescribeSoarStrategyTasks](~~DescribeSoarStrategyTasks~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.strategy_task_id = strategy_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strategy_task_id is not None:
            result['StrategyTaskId'] = self.strategy_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyTaskId') is not None:
            self.strategy_task_id = m.get('StrategyTaskId')

        return self

