# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListTodosResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListTodosResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # Indicates whether more data is available.
        self.has_more = has_more
        # The list of to-do items on the current page.
        self.items = items
        # The effective maximum number of entries to return per page for the current request.
        self.max_results = max_results
        # The error description.
        self.message = message
        # The pagination token for the next page. This field is an empty string if no more data is available.
        self.next_token = next_token
        # The current page number.
        self.page = page
        # The effective number of entries per page.
        self.page_size = page_size
        # The request tracking ID.
        self.request_id = request_id
        # The total number of visible items under the filter conditions.
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
                temp_model = main_models.ListTodosResponseBodyItems()
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

class ListTodosResponseBodyItems(DaraModel):
    def __init__(
        self,
        assignee_count: int = None,
        completed_at: str = None,
        completed_by_user_id: str = None,
        completed_by_user_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_read: bool = None,
        message_id: str = None,
        my_assignee_status: str = None,
        my_display_state: str = None,
        priority: str = None,
        question_count: int = None,
        question_summaries: List[str] = None,
        source_context: Dict[str, Any] = None,
        source_type: str = None,
        status: str = None,
        title: str = None,
        todo_id: str = None,
    ):
        # The number of assignees.
        self.assignee_count = assignee_count
        # The completion time in the YYYY-MM-DD HH:mm:ss format (UTC+8).
        self.completed_at = completed_at
        # The user ID of the user who completed the item. This field is empty if the item is not completed.
        self.completed_by_user_id = completed_by_user_id
        # The name of the user who completed the item. This field is empty if the item is not completed.
        self.completed_by_user_name = completed_by_user_name
        # The creation time in the YYYY-MM-DD HH:mm:ss format (UTC+8).
        self.gmt_create = gmt_create
        # The last modification time in the YYYY-MM-DD HH:mm:ss format (UTC+8).
        self.gmt_modified = gmt_modified
        # Indicates whether the caller has read the item.
        self.is_read = is_read
        # The message ID of the assistant that sent the to-do item. This field is empty if there is no conversation source.
        self.message_id = message_id
        # The action status of the caller as an assignee.
        self.my_assignee_status = my_assignee_status
        # The list display status for the caller.
        self.my_display_state = my_display_state
        # The priority.
        self.priority = priority
        # The number of questions.
        self.question_count = question_count
        # The list of question summaries.
        self.question_summaries = question_summaries
        # The source context. This context is passed through as-is during creation.
        self.source_context = source_context
        # The source type of the to-do item.
        self.source_type = source_type
        # The primary status of the to-do item.
        self.status = status
        # The to-do title.
        self.title = title
        # The to-do ID.
        self.todo_id = todo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assignee_count is not None:
            result['assigneeCount'] = self.assignee_count

        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.completed_by_user_id is not None:
            result['completedByUserId'] = self.completed_by_user_id

        if self.completed_by_user_name is not None:
            result['completedByUserName'] = self.completed_by_user_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.is_read is not None:
            result['isRead'] = self.is_read

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.my_assignee_status is not None:
            result['myAssigneeStatus'] = self.my_assignee_status

        if self.my_display_state is not None:
            result['myDisplayState'] = self.my_display_state

        if self.priority is not None:
            result['priority'] = self.priority

        if self.question_count is not None:
            result['questionCount'] = self.question_count

        if self.question_summaries is not None:
            result['questionSummaries'] = self.question_summaries

        if self.source_context is not None:
            result['sourceContext'] = self.source_context

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assigneeCount') is not None:
            self.assignee_count = m.get('assigneeCount')

        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('completedByUserId') is not None:
            self.completed_by_user_id = m.get('completedByUserId')

        if m.get('completedByUserName') is not None:
            self.completed_by_user_name = m.get('completedByUserName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('isRead') is not None:
            self.is_read = m.get('isRead')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('myAssigneeStatus') is not None:
            self.my_assignee_status = m.get('myAssigneeStatus')

        if m.get('myDisplayState') is not None:
            self.my_display_state = m.get('myDisplayState')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('questionCount') is not None:
            self.question_count = m.get('questionCount')

        if m.get('questionSummaries') is not None:
            self.question_summaries = m.get('questionSummaries')

        if m.get('sourceContext') is not None:
            self.source_context = m.get('sourceContext')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

