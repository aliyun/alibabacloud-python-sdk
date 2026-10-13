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
        # The list of caller numbers. If not specified, all numbers bound to the instance are selected by default.
        self.calling_number = calling_number
        # The configuration parameters for flash SMS push in JSON format, including the configuration information of third-party flash SMS.  
        # - templateId: the flash SMS template ID.  
        # - configId: the flash SMS configuration ID.
        # - templateContent: the flash SMS content.
        # 
        # > The value of templateContent must be obtained from the corresponding flash SMS capability partner.
        self.flash_sms_extras = flash_sms_extras
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The description of the job.
        self.job_group_description = job_group_description
        # The name of the job.
        # 
        # This parameter is required.
        self.job_group_name = job_group_name
        # The guaranteed concurrency.  
        # - When the job starts, a minimum of N concurrent calls are guaranteed.
        # - The sum of guaranteed concurrency for jobs of the same priority cannot exceed the instance concurrency.  
        # - If the guaranteed concurrency is set to 0, the system intelligently allocates idle concurrency.
        self.min_concurrency = min_concurrency
        # The priority of the job group. Valid values:
        # - **Urgent**: urgent job.
        # - **Daily**: daily job.
        self.priority = priority
        # The list of caller numbers for redialing.
        self.recall_calling_number = recall_calling_number
        # The redial strategy in JSON format. The default value of the parameters in the JSON object is false.
        # 
        # - **emptyNumberIgnore**: specifies whether to skip nonexistent numbers.
        # - **inArrearsIgnore**: specifies whether to skip numbers with overdue payments.
        # - **outOfServiceIgnore**: specifies whether to skip suspended numbers.
        self.recall_strategy_json = recall_strategy_json
        # The optimal ringing duration. Default value: 25.
        self.ringing_duration = ringing_duration
        # **[Deprecated]**
        self.scenario_id = scenario_id
        # The scenario ID.
        self.script_id = script_id
        # The execution strategy of the job.  
        # - repeatBy: the repetition type. Valid values: Once (no repetition), Week (weekly repetition), and Month (monthly repetition).  
        # - startTime: the start time of the time-based strategy.
        # - endTime: the end time of the time-based strategy.  
        # > Execution methods:
        # > - If the start and end times of the strategy are not specified, the execution method is immediate execution.
        # > - If the strategy time is specified, the job is executed based on the time, and the repetition type repeatBy must be selected.
        # - workingTime: the time period during which outbound calls can be made.
        # - maxAttemptsPerDay: the maximum number of call attempts per day for numbers under this job.
        # - minAttemptInterval: the retry interval for numbers, in minutes.
        # - routingStrategy: the number strategy. Valid values: None (not specified), LocalFirst (local numbers first), and LocalProvinceFirst (local province numbers first).
        # - repeatDays: the execution days corresponding to the repetition type. If the repetition type RepeatBy is Week, 0 represents Sunday, and 1 to 6 represent Monday to Saturday. If the repetition cycle RepeatBy is Month, 1 to 31 represent the 1st to the 31st day. Months without the specified date are not executed. For example, if the 30th is selected, the job is not executed in February.
        # - repeatable: specifies whether to enable cyclic jobs. Valid values: true and false.
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

