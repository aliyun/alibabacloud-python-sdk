# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeScheduledTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        tasks: List[main_models.DescribeScheduledTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # The status code of the operation.
        self.code = code
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The pagination token that indicates the position from which to start reading. Leave this parameter empty to read from the beginning.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of scheduled tasks.
        self.tasks = tasks
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.DescribeScheduledTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeScheduledTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_ids: List[str] = None,
        last_execution_at: str = None,
        next_execution_at: str = None,
        run_config: main_models.DescribeScheduledTasksResponseBodyTasksRunConfig = None,
        scheduled_id: str = None,
        status: str = None,
        task_config_id: str = None,
        task_name: str = None,
        total_executions: int = None,
        total_failures: int = None,
        user_prompt: str = None,
        version: int = None,
    ):
        # The cron expression.
        self.cron_expression = cron_expression
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The list of associated instance IDs.
        self.instance_ids = instance_ids
        # The last execution time.
        self.last_execution_at = last_execution_at
        # The next execution time.
        self.next_execution_at = next_execution_at
        # The run configuration.
        self.run_config = run_config
        # The scheduled task ID.
        self.scheduled_id = scheduled_id
        # The status.
        self.status = status
        # The task configuration ID.
        self.task_config_id = task_config_id
        # The task name.
        self.task_name = task_name
        # The total number of executions.
        self.total_executions = total_executions
        # The total number of failures.
        self.total_failures = total_failures
        # The user prompt or task description.
        self.user_prompt = user_prompt
        # The CAS version number.
        self.version = version

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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.last_execution_at is not None:
            result['LastExecutionAt'] = self.last_execution_at

        if self.next_execution_at is not None:
            result['NextExecutionAt'] = self.next_execution_at

        if self.run_config is not None:
            result['RunConfig'] = self.run_config.to_map()

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_config_id is not None:
            result['TaskConfigId'] = self.task_config_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.total_executions is not None:
            result['TotalExecutions'] = self.total_executions

        if self.total_failures is not None:
            result['TotalFailures'] = self.total_failures

        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LastExecutionAt') is not None:
            self.last_execution_at = m.get('LastExecutionAt')

        if m.get('NextExecutionAt') is not None:
            self.next_execution_at = m.get('NextExecutionAt')

        if m.get('RunConfig') is not None:
            temp_model = main_models.DescribeScheduledTasksResponseBodyTasksRunConfig()
            self.run_config = temp_model.from_map(m.get('RunConfig'))

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskConfigId') is not None:
            self.task_config_id = m.get('TaskConfigId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TotalExecutions') is not None:
            self.total_executions = m.get('TotalExecutions')

        if m.get('TotalFailures') is not None:
            self.total_failures = m.get('TotalFailures')

        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeScheduledTasksResponseBodyTasksRunConfig(DaraModel):
    def __init__(
        self,
        extra_params: str = None,
        max_steps: int = None,
        timeout_seconds: int = None,
    ):
        # The extra parameters.
        self.extra_params = extra_params
        # The maximum number of steps.
        self.max_steps = max_steps
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

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')

        if m.get('MaxSteps') is not None:
            self.max_steps = m.get('MaxSteps')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

