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
        # 业务状态码；成功为200
        self.code = code
        # 是否还有更多数据
        self.has_more = has_more
        # 当前页待办列表
        self.items = items
        # 本次生效的单页最大返回数量
        self.max_results = max_results
        # 错误描述
        self.message = message
        # 下一页翻页令牌；无更多数据时为空字符串
        self.next_token = next_token
        # 当前页码
        self.page = page
        # 生效单页条数
        self.page_size = page_size
        # 请求追踪ID
        self.request_id = request_id
        # 筛选条件下可见总数
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
        # 处理人数量
        self.assignee_count = assignee_count
        # 完成时间（北京时间 YYYY-MM-DD HH:mm:ss）
        self.completed_at = completed_at
        # 完成人用户ID；未完成为空
        self.completed_by_user_id = completed_by_user_id
        # 完成人姓名；未完成为空
        self.completed_by_user_name = completed_by_user_name
        # 创建时间（北京时间 YYYY-MM-DD HH:mm:ss）
        self.gmt_create = gmt_create
        # 最后修改时间（北京时间 YYYY-MM-DD HH:mm:ss）
        self.gmt_modified = gmt_modified
        # 调用者是否已读
        self.is_read = is_read
        # 发出该待办的 assistant 消息ID；无会话来源为空
        self.message_id = message_id
        # 调用者的处理人行状态
        self.my_assignee_status = my_assignee_status
        # 调用者的列表展示状态
        self.my_display_state = my_display_state
        # 优先级
        self.priority = priority
        # 问题数量
        self.question_count = question_count
        # 问题摘要列表
        self.question_summaries = question_summaries
        # 来源上下文（创建时原样透传）
        self.source_context = source_context
        # 待办来源类型
        self.source_type = source_type
        # 待办主状态
        self.status = status
        # 待办标题
        self.title = title
        # 待办ID
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

