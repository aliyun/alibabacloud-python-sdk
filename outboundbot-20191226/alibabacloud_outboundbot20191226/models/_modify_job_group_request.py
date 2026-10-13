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
        # The caller number.
        self.calling_number = calling_number
        # The job description.
        self.description = description
        # The configuration parameters for flash message push in JSON format, including the configuration information of third-party flash messages.
        # 
        # templateId: the flash message template ID.  
        # configId: the flash message configuration ID.
        self.flash_sms_extras = flash_sms_extras
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The job ID.
        # 
        # This parameter is required.
        self.job_group_id = job_group_id
        # The job status. Valid values:
        # - Draft: draft.
        # - Paused: paused.
        self.job_group_status = job_group_status
        # The guaranteed concurrency.
        # When a job starts, a minimum of N concurrent calls are guaranteed.
        # The sum of guaranteed concurrency values for jobs of the same priority cannot exceed the instance concurrency.
        # If the guaranteed concurrency is set to 0, the system intelligently allocates idle concurrency.
        self.min_concurrency = min_concurrency
        # The job name.
        # 
        # This parameter is required.
        self.name = name
        # The job group priority. Valid values:
        # - **Urgent**: urgent job.
        # - **Daily**: daily job.
        self.priority = priority
        # The list of caller numbers for recall.
        self.recall_calling_number = recall_calling_number
        # The JSON string of the recall strategy.
        self.recall_strategy_json = recall_strategy_json
        # The optimal ringing duration.
        self.ringing_duration = ringing_duration
        # The scenario ID. This is a legacy parameter. Use ScriptId instead.
        # 
        # > This parameter is a legacy parameter. You can pass any value. Keep it consistent with the ScriptId.
        self.scenario_id = scenario_id
        # The script ID.
        self.script_id = script_id
        # The job execution strategy.
        # - id: the job group strategy ID. You can obtain it from the StrategyId response parameter of the DescribeJobGroup operation.
        # - repeatBy: the recurrence type. Valid values: Once (no recurrence), Day (daily), Week (weekly), and Month (monthly).
        # - startTime: the start time of the strategy.
        # - endTime: the end time of the strategy.
        # - workingTime: the time period during which outbound calls are allowed.
        # - maxAttemptsPerDay: the maximum number of call attempts per day for a phone number under this job.
        # - minAttemptInterval: the retry interval for a phone number, in minutes.
        # - routingStrategy: the phone number strategy. Valid values: None (not specified), LocalFirst (local numbers first), and LocalProvinceFirst (local province numbers first).
        # - repeatDays: the execution days corresponding to the recurrence type. If RepeatBy is Week, 0 indicates Sunday, and 1 to 6 indicate Monday to Saturday. If RepeatBy is Month, 1 to 31 indicate the 1st to the 31st day of the month. If a month does not have the specified day, the job is not executed in that month. For example, if the 30th is selected, the job is not executed in February.
        # - repeatable: specifies whether to enable recurring jobs. Valid values: true and false.
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

