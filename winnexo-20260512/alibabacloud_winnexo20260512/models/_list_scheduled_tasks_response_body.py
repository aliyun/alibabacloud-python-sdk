# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListScheduledTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListScheduledTasksResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The status code.
        self.code = code
        # Indicates whether more data is available. Valid values: true (yes) and false (no).
        self.has_more = has_more
        # The list of skill cards.
        self.items = items
        # The maximum number of records to return for this request.
        self.max_results = max_results
        # The description of the status code.
        self.message = message
        # The pagination cursor.
        self.next_token = next_token
        # The specified page number. Default value: 1.
        self.page = page
        # The number of records per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of tasks.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
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

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListScheduledTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListScheduledTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        abnormal_reason: str = None,
        auto_preference: str = None,
        can_delete: bool = None,
        can_edit: bool = None,
        can_execute: bool = None,
        can_toggle: bool = None,
        collaboration_group_id: str = None,
        creator: str = None,
        creator_name: str = None,
        cron_expression: str = None,
        description: str = None,
        digital_employee_name: List[str] = None,
        execution_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_open: bool = None,
        model: str = None,
        name: str = None,
        output_mode: str = None,
        status: str = None,
        task_id: str = None,
        trigger_type: str = None,
        visibility: str = None,
        visible_member_user_ids: List[str] = None,
    ):
        # The cause of the exception. This field has a value only when status is abnormal.
        self.abnormal_reason = abnormal_reason
        # 任务 AUTO 偏好：none=默认、performance=效果优先、credit=成本优先
        self.auto_preference = auto_preference
        # Indicates whether the current caller can delete the task. This is valid only for the task creator and group owner. For personal tasks, the value is always true.
        self.can_delete = can_delete
        # Indicates whether the course can be edited or deleted.
        self.can_edit = can_edit
        # Indicates whether the current caller can immediately execute the task. Visible means operable. For abnormal tasks, the value is false. For personal tasks, the value is always true.
        self.can_execute = can_execute
        # Indicates whether the current caller can start or stop the task. This is valid only for the task creator and group owner. For abnormal tasks, the value is false. For personal tasks, the value is always true.
        self.can_toggle = can_toggle
        # The ID of the collaboration group to which the task belongs, such as cg_101. If this parameter is specified, a group space task is created, and the caller must be a valid group member. If this parameter is left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The creator.
        self.creator = creator
        # The creator.
        self.creator_name = creator_name
        # The cron expression.
        self.cron_expression = cron_expression
        # The description of the to-do card type.
        self.description = description
        # The list of digital employee names.
        self.digital_employee_name = digital_employee_name
        # The cumulative number of executions.
        self.execution_count = execution_count
        # The creation time.
        self.gmt_create = gmt_create
        # The last update time.
        self.gmt_modified = gmt_modified
        # Indicates whether public access is enabled.
        self.is_open = is_open
        # The execution model tier. If this parameter is not specified, the model tier is not updated.
        self.model = model
        # The name.
        self.name = name
        # The task output session mode.
        self.output_mode = output_mode
        # The task status. Running is returned immediately after submission.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The type of the trigger.
        self.trigger_type = trigger_type
        # The visibility scope of the group task. Valid values: PRIVATE (visible only to the creator and group owner), COLLABORATIVE (visible to specified collaboration members), and PUBLIC (visible to all group members). Default value for group tasks: PRIVATE. This field is ignored for personal tasks.
        self.visibility = visibility
        # The list of collaboration members, excluding the task creator and group creator, which are covered by the authentication layer. This field is returned only for group tasks. An empty list is returned for PRIVATE or PUBLIC visibility scopes.
        self.visible_member_user_ids = visible_member_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_reason is not None:
            result['abnormalReason'] = self.abnormal_reason

        if self.auto_preference is not None:
            result['autoPreference'] = self.auto_preference

        if self.can_delete is not None:
            result['canDelete'] = self.can_delete

        if self.can_edit is not None:
            result['canEdit'] = self.can_edit

        if self.can_execute is not None:
            result['canExecute'] = self.can_execute

        if self.can_toggle is not None:
            result['canToggle'] = self.can_toggle

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.creator is not None:
            result['creator'] = self.creator

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.description is not None:
            result['description'] = self.description

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.execution_count is not None:
            result['executionCount'] = self.execution_count

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.is_open is not None:
            result['isOpen'] = self.is_open

        if self.model is not None:
            result['model'] = self.model

        if self.name is not None:
            result['name'] = self.name

        if self.output_mode is not None:
            result['outputMode'] = self.output_mode

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        if self.visibility is not None:
            result['visibility'] = self.visibility

        if self.visible_member_user_ids is not None:
            result['visibleMemberUserIds'] = self.visible_member_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abnormalReason') is not None:
            self.abnormal_reason = m.get('abnormalReason')

        if m.get('autoPreference') is not None:
            self.auto_preference = m.get('autoPreference')

        if m.get('canDelete') is not None:
            self.can_delete = m.get('canDelete')

        if m.get('canEdit') is not None:
            self.can_edit = m.get('canEdit')

        if m.get('canExecute') is not None:
            self.can_execute = m.get('canExecute')

        if m.get('canToggle') is not None:
            self.can_toggle = m.get('canToggle')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('executionCount') is not None:
            self.execution_count = m.get('executionCount')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('isOpen') is not None:
            self.is_open = m.get('isOpen')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputMode') is not None:
            self.output_mode = m.get('outputMode')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        if m.get('visibleMemberUserIds') is not None:
            self.visible_member_user_ids = m.get('visibleMemberUserIds')

        return self

