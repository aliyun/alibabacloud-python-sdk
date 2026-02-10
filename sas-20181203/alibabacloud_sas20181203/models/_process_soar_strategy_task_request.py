# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProcessSoarStrategyTaskRequest(DaraModel):
    def __init__(
        self,
        strategy_task_id: int = None,
        task_action: str = None,
    ):
        # ID of the strategy task.
        # > You can obtain this parameter by calling the [DescribeSoarStrategyTasks](~~DescribeSoarStrategyTasks~~) interface.
        # 
        # This parameter is required.
        self.strategy_task_id = strategy_task_id
        # Task action status. Values:
        # - SCHEDULE: Schedule
        # - PAUSE: Pause
        # 
        # This parameter is required.
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strategy_task_id is not None:
            result['StrategyTaskId'] = self.strategy_task_id

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyTaskId') is not None:
            self.strategy_task_id = m.get('StrategyTaskId')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        return self

