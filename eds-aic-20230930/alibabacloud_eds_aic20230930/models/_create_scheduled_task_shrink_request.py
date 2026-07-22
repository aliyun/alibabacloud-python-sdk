# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateScheduledTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        instance_ids: List[str] = None,
        max_executions: int = None,
        run_config_shrink: str = None,
        task_name: str = None,
        user_prompt: str = None,
    ):
        # This parameter is required.
        self.cron_expression = cron_expression
        # This parameter is required.
        self.instance_ids = instance_ids
        self.max_executions = max_executions
        self.run_config_shrink = run_config_shrink
        # This parameter is required.
        self.task_name = task_name
        # This parameter is required.
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

        if self.max_executions is not None:
            result['MaxExecutions'] = self.max_executions

        if self.run_config_shrink is not None:
            result['RunConfig'] = self.run_config_shrink

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxExecutions') is not None:
            self.max_executions = m.get('MaxExecutions')

        if m.get('RunConfig') is not None:
            self.run_config_shrink = m.get('RunConfig')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        return self

