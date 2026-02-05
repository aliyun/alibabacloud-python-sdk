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
        self.calling_number = calling_number
        self.description = description
        self.flash_sms_extras = flash_sms_extras
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_group_id = job_group_id
        self.job_group_status = job_group_status
        self.min_concurrency = min_concurrency
        # This parameter is required.
        self.name = name
        self.priority = priority
        self.recall_calling_number = recall_calling_number
        self.recall_strategy_json = recall_strategy_json
        self.ringing_duration = ringing_duration
        self.scenario_id = scenario_id
        self.script_id = script_id
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

