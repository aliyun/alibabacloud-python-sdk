# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyScheduledTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        instance_ids: List[str] = None,
        run_config_shrink: str = None,
        scheduled_id: str = None,
        status: str = None,
        task_name: str = None,
        task_version: int = None,
        user_prompt: str = None,
    ):
        # The cron expression.
        self.cron_expression = cron_expression
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The run configuration.
        self.run_config_shrink = run_config_shrink
        # The scheduled task ID.
        # 
        # This parameter is required.
        self.scheduled_id = scheduled_id
        # The status switch: ACTIVE/DISABLED.
        self.status = status
        # The task name.
        self.task_name = task_name
        # The CAS version number.
        # 
        # This parameter is required.
        self.task_version = task_version
        # The user prompt.
        self.user_prompt = user_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.run_config_shrink is not None:
            result['RunConfig'] = self.run_config_shrink

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_version is not None:
            result['TaskVersion'] = self.task_version

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RunConfig') is not None:
            self.run_config_shrink = m.get('RunConfig')

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        return self

