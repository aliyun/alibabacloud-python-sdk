# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetScheduledTaskExecutionRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        tasks: List[main_models.GetScheduledTaskExecutionRecordsResponseBodyTasks] = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        self.tasks = tasks

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
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.tasks = []
        if m.get('tasks') is not None:
            for k1 in m.get('tasks'):
                temp_model = main_models.GetScheduledTaskExecutionRecordsResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class GetScheduledTaskExecutionRecordsResponseBodyTasks(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        description: str = None,
        is_open: bool = None,
        name: str = None,
        task_id: str = None,
        timeline: List[main_models.GetScheduledTaskExecutionRecordsResponseBodyTasksTimeline] = None,
        timezone: str = None,
        trigger_type: str = None,
    ):
        # Cron 表达式
        self.cron_expression = cron_expression
        # 任务简述
        self.description = description
        # 是否公开
        self.is_open = is_open
        # 文件名
        self.name = name
        # 任务 ID
        self.task_id = task_id
        self.timeline = timeline
        # 时区
        self.timezone = timezone
        # 触发类型 cron/manual/event
        self.trigger_type = trigger_type

    def validate(self):
        if self.timeline:
            for v1 in self.timeline:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.description is not None:
            result['description'] = self.description

        if self.is_open is not None:
            result['isOpen'] = self.is_open

        if self.name is not None:
            result['name'] = self.name

        if self.task_id is not None:
            result['taskId'] = self.task_id

        result['timeline'] = []
        if self.timeline is not None:
            for k1 in self.timeline:
                result['timeline'].append(k1.to_map() if k1 else None)

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isOpen') is not None:
            self.is_open = m.get('isOpen')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        self.timeline = []
        if m.get('timeline') is not None:
            for k1 in m.get('timeline'):
                temp_model = main_models.GetScheduledTaskExecutionRecordsResponseBodyTasksTimeline()
                self.timeline.append(temp_model.from_map(k1))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

class GetScheduledTaskExecutionRecordsResponseBodyTasksTimeline(DaraModel):
    def __init__(
        self,
        actual_time: str = None,
        display_name: str = None,
        error_message: str = None,
        execution_id: str = None,
        output_content: str = None,
        scheduled_time: str = None,
        status: str = None,
    ):
        # 实际执行时间（仅历史记录）
        self.actual_time = actual_time
        # 执行记录展示名称
        self.display_name = display_name
        # 错误信息（仅失败记录）
        self.error_message = error_message
        # 执行记录 ID（历史记录才有）
        self.execution_id = execution_id
        # 执行输出内容（仅历史记录）
        self.output_content = output_content
        # 计划执行时间 ISO8601
        self.scheduled_time = scheduled_time
        # 状态：PENDING/RUNNING/SUCCESS/FAILED/SCHEDULED
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_time is not None:
            result['actualTime'] = self.actual_time

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.execution_id is not None:
            result['executionId'] = self.execution_id

        if self.output_content is not None:
            result['outputContent'] = self.output_content

        if self.scheduled_time is not None:
            result['scheduledTime'] = self.scheduled_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actualTime') is not None:
            self.actual_time = m.get('actualTime')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')

        if m.get('outputContent') is not None:
            self.output_content = m.get('outputContent')

        if m.get('scheduledTime') is not None:
            self.scheduled_time = m.get('scheduledTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

