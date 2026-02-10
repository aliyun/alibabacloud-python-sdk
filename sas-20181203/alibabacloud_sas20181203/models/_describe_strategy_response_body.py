# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeStrategyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        strategies: List[main_models.DescribeStrategyResponseBodyStrategies] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The details of the baseline check policies.
        self.strategies = strategies

    def validate(self):
        if self.strategies:
            for v1 in self.strategies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Strategies'] = []
        if self.strategies is not None:
            for k1 in self.strategies:
                result['Strategies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.strategies = []
        if m.get('Strategies') is not None:
            for k1 in m.get('Strategies'):
                temp_model = main_models.DescribeStrategyResponseBodyStrategies()
                self.strategies.append(temp_model.from_map(k1))

        return self

class DescribeStrategyResponseBodyStrategies(DaraModel):
    def __init__(
        self,
        config_targets: List[main_models.DescribeStrategyResponseBodyStrategiesConfigTargets] = None,
        custom_type: str = None,
        cycle_days: int = None,
        cycle_start_time: int = None,
        ecs_count: int = None,
        end_time: str = None,
        exec_status: int = None,
        execution_type: str = None,
        id: int = None,
        name: str = None,
        pass_rate: int = None,
        percent: str = None,
        process_rate: int = None,
        risk_count: int = None,
        start_time: str = None,
        type: int = None,
        user_modify_time: int = None,
    ):
        # The details of the assets to which the baseline check policy is applied.
        self.config_targets = config_targets
        # The type of the baseline check policy. Valid values:
        # 
        # *   **common**
        # *   **custom**
        self.custom_type = custom_type
        # The cycle of the baseline check. Valid values:
        # 
        # *   **1**: every 2 days
        # *   **3**: every 4 days
        # *   **7**: every 8 days
        # *   30: every 31 days
        self.cycle_days = cycle_days
        # The time when the baseline check starts. Valid values:
        # 
        # *   **0**: The baseline check starts within the time range from 00:00 to 06:00.
        # *   **6**: The baseline check starts within the time range from 06:00 to 12:00.
        # *   **12**: The baseline check starts within the time range from 12:00 to 18:00.
        # *   **18**: The baseline check starts within the time range from 18:00 to 24:00.
        self.cycle_start_time = cycle_start_time
        # The number of the assets to which the baseline check policy is applied.
        self.ecs_count = ecs_count
        # The end time of the baseline check policy.
        self.end_time = end_time
        # The status of the baseline check policy. Valid values:
        # 
        # *   **1**: not executed
        # *   **2**: executing
        self.exec_status = exec_status
        # The triggering method of baseline scanning. Value:
        # 
        # - **Schedule** : Periodic configuration of task triggers
        # 
        # - **Manual** : Manually triggered
        self.execution_type = execution_type
        # The ID of the baseline check policy.
        self.id = id
        # The name of the baseline check policy.
        self.name = name
        # The proportion of risky baselines in the baseline check result.
        self.pass_rate = pass_rate
        # The progress of the baseline check by using the baseline. This parameter is returned only if the value of the ExecStatus parameter is 2.
        self.percent = percent
        # The number of the assets on which the baseline check is complete.
        self.process_rate = process_rate
        # The number of baseline check items in the baseline check policy.
        self.risk_count = risk_count
        # The start time of the baseline check policy.
        self.start_time = start_time
        # The source type of the baseline check policy. Valid values:
        # 
        # *   **1**: indicates a built-in policy provided and performed by Security Center by default.
        # *   **2**: indicates a user-defined policy. It can be a standard or custom baseline check policy.
        self.type = type
        # The time when the baseline check policy was last modified.
        self.user_modify_time = user_modify_time

    def validate(self):
        if self.config_targets:
            for v1 in self.config_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigTargets'] = []
        if self.config_targets is not None:
            for k1 in self.config_targets:
                result['ConfigTargets'].append(k1.to_map() if k1 else None)

        if self.custom_type is not None:
            result['CustomType'] = self.custom_type

        if self.cycle_days is not None:
            result['CycleDays'] = self.cycle_days

        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time

        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.exec_status is not None:
            result['ExecStatus'] = self.exec_status

        if self.execution_type is not None:
            result['ExecutionType'] = self.execution_type

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.pass_rate is not None:
            result['PassRate'] = self.pass_rate

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.process_rate is not None:
            result['ProcessRate'] = self.process_rate

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        if self.user_modify_time is not None:
            result['UserModifyTime'] = self.user_modify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_targets = []
        if m.get('ConfigTargets') is not None:
            for k1 in m.get('ConfigTargets'):
                temp_model = main_models.DescribeStrategyResponseBodyStrategiesConfigTargets()
                self.config_targets.append(temp_model.from_map(k1))

        if m.get('CustomType') is not None:
            self.custom_type = m.get('CustomType')

        if m.get('CycleDays') is not None:
            self.cycle_days = m.get('CycleDays')

        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')

        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecStatus') is not None:
            self.exec_status = m.get('ExecStatus')

        if m.get('ExecutionType') is not None:
            self.execution_type = m.get('ExecutionType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PassRate') is not None:
            self.pass_rate = m.get('PassRate')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('ProcessRate') is not None:
            self.process_rate = m.get('ProcessRate')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserModifyTime') is not None:
            self.user_modify_time = m.get('UserModifyTime')

        return self

class DescribeStrategyResponseBodyStrategiesConfigTargets(DaraModel):
    def __init__(
        self,
        flag: str = None,
        target: str = None,
        target_type: str = None,
    ):
        # Indicates whether the baseline check policy is applied to the asset group. Valid values:
        # 
        # *   **add**: The baseline check policy is applied to the asset group.
        # *   **del**: the baseline check policy is not applied to the asset group.
        self.flag = flag
        # The asset group ID or UUID of the asset to which the baseline check policy is applied.
        self.target = target
        # The condition by which the baseline check policy is applied to the asset. Valid values:
        # 
        # *   **groupId**: the ID of the asset group
        # *   **uuid**: the UUID of the asset
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flag is not None:
            result['Flag'] = self.flag

        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

