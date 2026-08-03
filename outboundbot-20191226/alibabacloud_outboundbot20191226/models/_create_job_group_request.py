# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateJobGroupRequest(DaraModel):
    def __init__(
        self,
        calling_number: List[str] = None,
        flash_sms_extras: str = None,
        instance_id: str = None,
        job_group_description: str = None,
        job_group_name: str = None,
        min_concurrency: int = None,
        priority: str = None,
        recall_calling_number: List[str] = None,
        recall_strategy_json: str = None,
        ringing_duration: int = None,
        scenario_id: str = None,
        script_id: str = None,
        strategy_json: str = None,
    ):
        # The list of calling numbers. If not specified, all numbers bound to the instance are selected by default.
        self.calling_number = calling_number
        # The configuration parameters for flash SMS in JSON format, including third-party flash SMS configuration information.  
        # - templateId: the flash SMS template ID.  
        # - configId: the flash SMS configuration ID.
        # - templateContent: the flash SMS content.
        # 
        # > Obtain the value of templateContent from the corresponding flash SMS capability provider.
        self.flash_sms_extras = flash_sms_extras
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The task description.
        self.job_group_description = job_group_description
        # The task name.
        # 
        # This parameter is required.
        self.job_group_name = job_group_name
        # The guaranteed concurrency value.  
        # - When the task starts, a minimum of N concurrent calls are guaranteed.
        # - The sum of guaranteed concurrency values for tasks with the same priority cannot exceed the instance concurrency.  
        # - If the guaranteed concurrency value is set to 0, the system intelligently allocates idle concurrency.
        self.min_concurrency = min_concurrency
        # The job group priority. Valid values:
        # - **Urgent**: urgent task.
        # - **Daily**: daily task.
        self.priority = priority
        # The list of redial calling numbers.
        self.recall_calling_number = recall_calling_number
        # The redial strategy in JSON format. Parameter values default to false.
        # 
        # - **emptyNumberIgnore**: does not call nonexistent numbers.
        # - **inArrearsIgnore**: does not call numbers with overdue payments.
        # - **outOfServiceIgnore**: does not call numbers that are out of service.
        self.recall_strategy_json = recall_strategy_json
        # The optimal ringing duration. Default value: 25.
        self.ringing_duration = ringing_duration
        # Deprecated.
        self.scenario_id = scenario_id
        # The scenario ID.
        self.script_id = script_id
        # The task execution strategy.  
        # - repeatBy: the repeat type. Valid values: Once (no repeat), Week (repeat weekly), and Month (repeat monthly).  
        # - startTime: the strategy start time for time-based execution.
        # - endTime: the strategy end time for time-based execution.  
        # > The execution mode is determined as follows:
        # > - If no strategy start time or end time is specified, the task is executed immediately.
        # > - If a strategy time is specified, the task is executed based on the schedule. You must also specify the repeat type repeatBy.
        # - workingTime: the time window during which outbound calls can be made.
        # - maxAttemptsPerDay: the maximum number of call attempts per day for each number in the task.
        # - minAttemptInterval: the retry interval for a number, in minutes.
        # - routingStrategy: the number strategy. Valid values: None (not specified), LocalFirst (local city numbers preferred), and LocalProvinceFirst (local province numbers preferred).
        # - repeatDays: the execution days corresponding to the repeat type. If RepeatBy is set to Week, 0 indicates Sunday and 1-6 indicate Monday through Saturday. If RepeatBy is set to Month, 1-31 indicate the 1st through 31st day. The task is not executed in months that do not have the specified day. For example, if the 30th is selected, the task is not executed in February.
        # - repeatable: specifies whether to enable cyclic tasks. Valid values: true and false.
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

        if self.flash_sms_extras is not None:
            result['FlashSmsExtras'] = self.flash_sms_extras

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description

        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name

        if self.min_concurrency is not None:
            result['MinConcurrency'] = self.min_concurrency

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

        if m.get('FlashSmsExtras') is not None:
            self.flash_sms_extras = m.get('FlashSmsExtras')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')

        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')

        if m.get('MinConcurrency') is not None:
            self.min_concurrency = m.get('MinConcurrency')

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

