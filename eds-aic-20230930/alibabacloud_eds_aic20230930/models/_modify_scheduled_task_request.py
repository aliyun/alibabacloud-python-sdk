# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ModifyScheduledTaskRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        instance_ids: List[str] = None,
        run_config: main_models.ModifyScheduledTaskRequestRunConfig = None,
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
        self.run_config = run_config
        # The scheduled task ID.
        # 
        # This parameter is required.
        self.scheduled_id = scheduled_id
        # Switches the status. Valid values: ACTIVE and DISABLED.
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
        if self.run_config:
            self.run_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.run_config is not None:
            result['RunConfig'] = self.run_config.to_map()

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
            temp_model = main_models.ModifyScheduledTaskRequestRunConfig()
            self.run_config = temp_model.from_map(m.get('RunConfig'))

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

class ModifyScheduledTaskRequestRunConfig(DaraModel):
    def __init__(
        self,
        extra_params: str = None,
        max_steps: int = None,
        skills: List[str] = None,
        timeout_seconds: int = None,
    ):
        # The extended parameter JSON string.
        self.extra_params = extra_params
        # The maximum number of execution steps.
        self.max_steps = max_steps
        # The list of skill IDs. A maximum of 1 skill ID is supported. The value overwrites aim_task_config.run_config after modification.
        self.skills = skills
        # The timeout period, in seconds.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params

        if self.max_steps is not None:
            result['MaxSteps'] = self.max_steps

        if self.skills is not None:
            result['Skills'] = self.skills

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')

        if m.get('MaxSteps') is not None:
            self.max_steps = m.get('MaxSteps')

        if m.get('Skills') is not None:
            self.skills = m.get('Skills')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

