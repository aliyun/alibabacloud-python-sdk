# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyJobGroupRequest(DaraModel):
    def __init__(
        self,
        calling_number: List[str] = None,
        description: str = None,
        flash_sms_extras: str = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_group_status: str = None,
        min_concurrency: int = None,
        name: str = None,
        priority: str = None,
        recall_calling_number: List[str] = None,
        recall_strategy_json: str = None,
        ringing_duration: int = None,
        scenario_id: str = None,
        script_id: str = None,
        strategy_json: str = None,
    ):
        # The calling numbers for the job group.
        self.calling_number = calling_number
        # The description of the job group.
        self.description = description
        # The flash SMS configuration, specified as a JSON string. This may include settings for third-party flash SMS services.
        # 
        # `templateId`: The flash SMS template ID.<br>
        # `configId`: The flash SMS configuration ID.<br>
        self.flash_sms_extras = flash_sms_extras
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The job group ID.
        # 
        # This parameter is required.
        self.job_group_id = job_group_id
        # The status of the job group. Valid values:
        # 
        # - `Draft`: The job group is in a draft state.
        # 
        # - `Paused`: The job group is paused.
        self.job_group_status = job_group_status
        # The guaranteed minimum number of concurrent calls for the job group. The sum of this value for all job groups with the same priority cannot exceed the instance\\"s total concurrency. If you set this parameter to `0`, the system dynamically allocates available lines from a shared pool.
        self.min_concurrency = min_concurrency
        # The name of the job group.
        # 
        # This parameter is required.
        self.name = name
        # The priority of the job group. Valid values:
        # 
        # - **Urgent**: An urgent job.
        # 
        # - **Daily**: A routine job.
        self.priority = priority
        # The recall calling numbers.
        self.recall_calling_number = recall_calling_number
        # A JSON string that defines the recall strategy.
        self.recall_strategy_json = recall_strategy_json
        # The optimal ringing duration.
        self.ringing_duration = ringing_duration
        # The scenario ID. (This is a legacy parameter. Use `ScriptId` instead.)
        # 
        # > You can pass any value for this legacy parameter, but we recommend using the same value as `ScriptId` for consistency.
        self.scenario_id = scenario_id
        # The ID of the script for the scenario.
        self.script_id = script_id
        # A JSON string that defines the execution strategy for the job group.
        # 
        # - `id`: The ID of the job group strategy. You can obtain this ID from the `StrategyId` parameter returned by the `DescribeJobGroup` operation.
        # 
        # - `repeatBy`: The frequency of the job. Valid values: `Once` (does not repeat), `Day` (repeats daily), `Week` (repeats weekly), and `Month` (repeats monthly).
        # 
        # - `startTime`: The start time of the strategy.
        # 
        # - `endTime`: The end time of the strategy.
        # 
        # - `workingTime`: The time windows for making outbound calls.
        # 
        # - `maxAttemptsPerDay`: The maximum number of call attempts per day for a number in this job group.
        # 
        # - `minAttemptInterval`: The minimum interval, in minutes, between call retries to the same number.
        # 
        # - `routingStrategy`: The number routing strategy. Valid values: `None` (not specified), `LocalFirst` (prioritizes numbers in the same city), and `LocalProvinceFirst` (prioritizes numbers in the same province).
        # 
        # - `repeatDays`: The specific days to run the job, based on the `repeatBy` value. If `repeatBy` is `Week`, `0` indicates Sunday, and `1` through `6` indicate Monday through Saturday. If `repeatBy` is `Month`, valid values are `1` through `31`. If a month does not have the specified day (for example, day 30 in February), the job does not run on that day.
        # 
        # - `repeatable`: Whether the job is recurring. Valid values are `true` and `false`.
        self.strategy_json = strategy_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.description is not None:
            result['Description'] = self.description

        if self.flash_sms_extras is not None:
            result['FlashSmsExtras'] = self.flash_sms_extras

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_group_status is not None:
            result['JobGroupStatus'] = self.job_group_status

        if self.min_concurrency is not None:
            result['MinConcurrency'] = self.min_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.recall_calling_number is not None:
            result['RecallCallingNumber'] = self.recall_calling_number

        if self.recall_strategy_json is not None:
            result['RecallStrategyJson'] = self.recall_strategy_json

        if self.ringing_duration is not None:
            result['RingingDuration'] = self.ringing_duration

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlashSmsExtras') is not None:
            self.flash_sms_extras = m.get('FlashSmsExtras')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobGroupStatus') is not None:
            self.job_group_status = m.get('JobGroupStatus')

        if m.get('MinConcurrency') is not None:
            self.min_concurrency = m.get('MinConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RecallCallingNumber') is not None:
            self.recall_calling_number = m.get('RecallCallingNumber')

        if m.get('RecallStrategyJson') is not None:
            self.recall_strategy_json = m.get('RecallStrategyJson')

        if m.get('RingingDuration') is not None:
            self.ringing_duration = m.get('RingingDuration')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')

        return self

