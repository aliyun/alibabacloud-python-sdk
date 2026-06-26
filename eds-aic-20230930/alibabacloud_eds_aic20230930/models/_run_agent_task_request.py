# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunAgentTaskRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        instance_ids: List[str] = None,
        max_steps: int = None,
        schedule_id: str = None,
        task_config_id: str = None,
        timeout_seconds: int = None,
        user_prompt: str = None,
    ):
        # The region ID of the Mobile node.
        self.biz_region_id = biz_region_id
        # The list of Mobile node IDs. A maximum of 100 nodes are supported per request.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The maximum number of execution steps for the task to prevent infinite loops. Valid values: 30 to 1000. Default value: 1000.
        self.max_steps = max_steps
        self.schedule_id = schedule_id
        self.task_config_id = task_config_id
        # The task timeout period in seconds. Valid values: 300 to 3600. Default value: 3600.
        self.timeout_seconds = timeout_seconds
        # The user instruction in natural language. The Agent performs operations based on this instruction.
        self.user_prompt = user_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.max_steps is not None:
            result['MaxSteps'] = self.max_steps

        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id

        if self.task_config_id is not None:
            result['TaskConfigId'] = self.task_config_id

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxSteps') is not None:
            self.max_steps = m.get('MaxSteps')

        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')

        if m.get('TaskConfigId') is not None:
            self.task_config_id = m.get('TaskConfigId')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        return self

