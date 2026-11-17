# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetScheduledTaskConversationRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[main_models.GetScheduledTaskConversationRecordsResponseBodyTasks] = None,
        total: int = None,
    ):
        # The response status code.
        self.code = code
        # Indicates whether a next page exists.
        self.has_more = has_more
        # The description of the status code.
        self.message = message
        # The page number. Default value: 1. Minimum value: 1. Maximum value: 200.
        self.page = page
        # The collaboration group ID, such as cg_101. If you specify this parameter, the data is returned by group dimension, and the caller must be a valid group member. If you do not specify this parameter, the data is returned by personal dimension, excluding group tasks.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of tasks.
        self.tasks = tasks
        # The total number of Logtail pipeline configurations in the current project.
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
                temp_model = main_models.GetScheduledTaskConversationRecordsResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetScheduledTaskConversationRecordsResponseBodyTasks(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        conversations: List[main_models.GetScheduledTaskConversationRecordsResponseBodyTasksConversations] = None,
        cron_expression: str = None,
        description: str = None,
        is_open: bool = None,
        model: str = None,
        name: str = None,
        task_id: str = None,
        timezone: str = None,
        trigger_type: str = None,
    ):
        # Pre-filters by a single task. If you do not specify this parameter, the execution records of all visible tasks are returned.
        self.collaboration_group_id = collaboration_group_id
        # The list of sessions.
        self.conversations = conversations
        # The cron expression.
        self.cron_expression = cron_expression
        # The description of the to-do card type.
        self.description = description
        # Indicates whether public access is enabled.
        self.is_open = is_open
        # The execution model tier. Valid values: flagship (Flagship), standard (Standard), and quick (Lightweight).
        self.model = model
        # The name.
        self.name = name
        # The task ID.
        self.task_id = task_id
        # The time zone.
        # 
        # > Default value: UTC+8.
        self.timezone = timezone
        # The trigger type. Valid values:
        # - Manual: Manual execution.
        # - Cron: Scheduled trigger.
        self.trigger_type = trigger_type

    def validate(self):
        if self.conversations:
            for v1 in self.conversations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        result['conversations'] = []
        if self.conversations is not None:
            for k1 in self.conversations:
                result['conversations'].append(k1.to_map() if k1 else None)

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

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        self.conversations = []
        if m.get('conversations') is not None:
            for k1 in m.get('conversations'):
                temp_model = main_models.GetScheduledTaskConversationRecordsResponseBodyTasksConversations()
                self.conversations.append(temp_model.from_map(k1))

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

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

class GetScheduledTaskConversationRecordsResponseBodyTasksConversations(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        display_name: str = None,
        has_unread: bool = None,
        latest_execution_id: str = None,
        latest_status: str = None,
        updated_at: str = None,
    ):
        # The actual group topic ID, which can be associated in queryWorkItemFeed. This ID cannot be used as a Workflow workItemId.
        self.conversation_id = conversation_id
        # The name of the schedule location.
        self.display_name = display_name
        # Indicates whether unread messages exist.
        self.has_unread = has_unread
        # The ID of the latest execution record.
        self.latest_execution_id = latest_execution_id
        # The latest execution status.
        self.latest_status = latest_status
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.has_unread is not None:
            result['hasUnread'] = self.has_unread

        if self.latest_execution_id is not None:
            result['latestExecutionId'] = self.latest_execution_id

        if self.latest_status is not None:
            result['latestStatus'] = self.latest_status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('hasUnread') is not None:
            self.has_unread = m.get('hasUnread')

        if m.get('latestExecutionId') is not None:
            self.latest_execution_id = m.get('latestExecutionId')

        if m.get('latestStatus') is not None:
            self.latest_status = m.get('latestStatus')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

