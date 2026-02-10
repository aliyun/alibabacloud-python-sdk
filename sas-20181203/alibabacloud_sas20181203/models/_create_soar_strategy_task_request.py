# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSoarStrategyTaskRequest(DaraModel):
    def __init__(
        self,
        strategy_id: int = None,
        strategy_name: str = None,
        strategy_task_name: str = None,
        strategy_task_params: str = None,
        strategy_task_plan_exe_time: int = None,
    ):
        # The ID of the policy.
        # 
        # >  You can call the [DescribeSoarSubscribedStrategy](~~DescribeSoarSubscribedStrategy~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.strategy_id = strategy_id
        # The name of the policy. Set the value to Automated Batch Vulnerability Fixing Policy for Multiple Servers.
        # 
        # This parameter is required.
        self.strategy_name = strategy_name
        # The name of.the policy task.
        # 
        # This parameter is required.
        self.strategy_task_name = strategy_task_name
        # The parameters of the policy task. The value is a JSON array.
        # 
        # Vulnerability-related parameters:
        # 
        # *   name: vluList
        # *   associationProperty: sasAllVul
        # *   value: basic vulnerability information
        # 
        # Snapshot-related parameters:
        # 
        # *   name: snapshotConfig
        # *   associationProperty: snapshotConfig
        # *   value: retention period
        # 
        # Notification-related parameters:
        # 
        # *   name: notifyConfig
        # *   associationProperty: notifyConfig
        # *   value: email or DingTalk configuration information
        # 
        # This parameter is required.
        self.strategy_task_params = strategy_task_params
        # The timestamp when the task is scheduled to start. Unit: milliseconds.
        self.strategy_task_plan_exe_time = strategy_task_plan_exe_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.strategy_task_name is not None:
            result['StrategyTaskName'] = self.strategy_task_name

        if self.strategy_task_params is not None:
            result['StrategyTaskParams'] = self.strategy_task_params

        if self.strategy_task_plan_exe_time is not None:
            result['StrategyTaskPlanExeTime'] = self.strategy_task_plan_exe_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StrategyTaskName') is not None:
            self.strategy_task_name = m.get('StrategyTaskName')

        if m.get('StrategyTaskParams') is not None:
            self.strategy_task_params = m.get('StrategyTaskParams')

        if m.get('StrategyTaskPlanExeTime') is not None:
            self.strategy_task_plan_exe_time = m.get('StrategyTaskPlanExeTime')

        return self

