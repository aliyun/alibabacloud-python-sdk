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
        # List of caller numbers. If not specified, all numbers attached to the instance are selected by default.
        self.calling_number = calling_number
        # Configuration parameters for flash SMS push, in JSON format, containing third-party flash SMS configuration information.  
        # - templateId: Flash SMS Template ID.  
        # - configId: Flash SMS configuration ID.  
        # - templateContent: Flash SMS Content.  
        # 
        # > Obtain the value of templateContent from the partner providing the flash SMS capability.
        self.flash_sms_extras = flash_sms_extras
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Task description.
        self.job_group_description = job_group_description
        # Task name.
        # 
        # This parameter is required.
        self.job_group_name = job_group_name
        # Concurrent guarantee value.  
        # - When a job starts, it is guaranteed a minimum of N concurrent executions.  
        # - The sum of concurrent guarantee values for jobs with the same priority must not exceed the instance concurrency limit.  
        # - If the concurrent guarantee value is configured as 0, the system intelligently assigns idle concurrency resources.
        self.min_concurrency = min_concurrency
        # Job group priority. Valid values:
        # - **Urgent**: Urgent job.
        # - **Daily**: Daily job.
        self.priority = priority
        # List of caller numbers for redial.
        self.recall_calling_number = recall_calling_number
        # Redial policy in JSON format. The default value of parameters in the JSON is false.
        # 
        # - **emptyNumberIgnore**: Do not make outbound calls to nonexistent numbers.
        # - **inArrearsIgnore**: Do not make outbound calls for overdue payments.
        # - **outOfServiceIgnore**: Do not make outbound calls to out-of-service numbers.
        self.recall_strategy_json = recall_strategy_json
        # Optimal ringing duration. Default value is 25.
        self.ringing_duration = ringing_duration
        # Deprecated
        self.scenario_id = scenario_id
        # Scenario ID.
        self.script_id = script_id
        # Job execution policy.  
        # - repeatBy: Recurrence type. Options are Once (no recurrence), Week (weekly recurrence), and Month (monthly recurrence).  
        # - startTime: Policy start time for time-based execution.  
        # - endTime: Policy end time for time-based execution.  
        # > Execution modes are as follows:  
        # > - If no start or end time is specified, the job executes immediately.  
        # > - If start and end times are provided, the job executes based on the schedule, and a recurrence type (repeatBy) must be selected.  
        # - workingTime: Allowed outbound calling time segment.  
        # - maxAttemptsPerDay: Maximum number of call attempts per day for numbers under this job.  
        # - minAttemptInterval: Minimum time interval between retry calls for a number, in minutes.  
        # - routingStrategy: Number routing strategy. Options are None (not specified), LocalFirst (local city numbers prioritized), and LocalProvinceFirst (local province numbers prioritized).  
        # - repeatDays: Execution dates corresponding to the recurrence type. If repeatBy is Week, 0 represents Sunday and 1–6 represent Monday through Saturday. If repeatBy is Month, values 1–31 represent the 1st through the 31st day of the month; months without the specified date skip execution (for example, if the 30th is selected, February skips execution).  
        # - repeatable: Whether loop task is enabled, true/false.
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

