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
        has_more: bool = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[main_models.GetScheduledTaskExecutionRecordsResponseBodyTasks] = None,
        total: int = None,
    ):
        # The status code.
        self.code = code
        # Indicates whether more data is available.
        self.has_more = has_more
        # The description of the status code.
        self.message = message
        # The current page number.
        self.page = page
        # The number of tasks per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The task list.
        self.tasks = tasks
        # The total number of tasks.
        self.total = total

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

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['tasks'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.tasks = []
        if m.get('tasks') is not None:
            for k1 in m.get('tasks'):
                temp_model = main_models.GetScheduledTaskExecutionRecordsResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetScheduledTaskExecutionRecordsResponseBodyTasks(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        cron_expression: str = None,
        description: str = None,
        is_open: bool = None,
        model: str = None,
        name: str = None,
        task_id: str = None,
        timeline: List[main_models.GetScheduledTaskExecutionRecordsResponseBodyTasksTimeline] = None,
        timezone: str = None,
        trigger_type: str = None,
    ):
        # The ID of the collaboration group to which the task belongs. If empty, the task is a personal task.
        self.collaboration_group_id = collaboration_group_id
        # The cron expression.
        self.cron_expression = cron_expression
        # The description of the to-do card type.
        self.description = description
        # Indicates whether public access is enabled.
        self.is_open = is_open
        # The execution model tier. Valid values:
        # - flagship: flagship.
        # - standard: standard.
        # - quick: lightweight.
        self.model = model
        # The name.
        self.name = name
        # The task ID.
        self.task_id = task_id
        # The timeline.
        self.timeline = timeline
        # The time zone.
        # 
        # > Default value: UTC+8.
        self.timezone = timezone
        # The trigger type. Valid values:
        # - Manual: manually executed.
        # - Cron: triggered by a schedule.
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
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.description is not None:
            result['description'] = self.description

        if self.is_open is not None:
            result['isOpen'] = self.is_open

        if self.model is not None:
            result['model'] = self.model

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
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isOpen') is not None:
            self.is_open = m.get('isOpen')

        if m.get('model') is not None:
            self.model = m.get('model')

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
        is_expired: bool = None,
        output_content: str = None,
        scheduled_time: str = None,
        status: str = None,
    ):
        # The actual working hours, in hours.
        self.actual_time = actual_time
        # The name of the schedule location.
        self.display_name = display_name
        # The error message.
        self.error_message = error_message
        # The execution record ID.
        self.execution_id = execution_id
        # Indicates whether the execution record has been archived due to expiration.
        self.is_expired = is_expired
        # The execution output content (historical records only).
        self.output_content = output_content
        # The timed scheduling time.
        self.scheduled_time = scheduled_time
        # The final status of the message.
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

        if self.is_expired is not None:
            result['isExpired'] = self.is_expired

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

        if m.get('isExpired') is not None:
            self.is_expired = m.get('isExpired')

        if m.get('outputContent') is not None:
            self.output_content = m.get('outputContent')

        if m.get('scheduledTime') is not None:
            self.scheduled_time = m.get('scheduledTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

