# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetWorkItemAuditResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.GetWorkItemAuditResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
    ):
        # 公共业务状态码
        self.code = code
        # 按事件时间倒序排列的完整工作项审计记录
        self.items = items
        # 公共错误描述
        self.message = message
        # 请求追踪ID
        self.request_id = request_id

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

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetWorkItemAuditResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetWorkItemAuditResponseBodyItems(DaraModel):
    def __init__(
        self,
        changes: Any = None,
        description: str = None,
        event_id: str = None,
        event_type: str = None,
        occurred_at: str = None,
        operator_name: str = None,
        operator_user_id: str = None,
        questions: List[Any] = None,
        result_payload: Any = None,
        status: str = None,
        title: str = None,
        todo_id: str = None,
    ):
        # 字段变更明细列表，每项包含变更字段与前后值
        self.changes = changes
        # 事件描述
        self.description = description
        # 审计事件唯一标识
        self.event_id = event_id
        # 审计事件类型，如 WORK_ITEM_UPDATED、TODO_COMPLETED
        self.event_type = event_type
        # 事件发生时间，ISO8601 格式
        self.occurred_at = occurred_at
        # 操作人显示名
        self.operator_name = operator_name
        # 操作人用户 ID
        self.operator_user_id = operator_user_id
        # 事件涉及的待确认问题列表
        self.questions = questions
        # 事件结果负载，JSON 对象；无结果时为空
        self.result_payload = result_payload
        # 事件状态
        self.status = status
        # 事件标题
        self.title = title
        # 关联待办 ID；无关联时为空字符串
        self.todo_id = todo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changes is not None:
            result['changes'] = self.changes

        if self.description is not None:
            result['description'] = self.description

        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.occurred_at is not None:
            result['occurredAt'] = self.occurred_at

        if self.operator_name is not None:
            result['operatorName'] = self.operator_name

        if self.operator_user_id is not None:
            result['operatorUserId'] = self.operator_user_id

        if self.questions is not None:
            result['questions'] = self.questions

        if self.result_payload is not None:
            result['resultPayload'] = self.result_payload

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changes') is not None:
            self.changes = m.get('changes')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('occurredAt') is not None:
            self.occurred_at = m.get('occurredAt')

        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')

        if m.get('operatorUserId') is not None:
            self.operator_user_id = m.get('operatorUserId')

        if m.get('questions') is not None:
            self.questions = m.get('questions')

        if m.get('resultPayload') is not None:
            self.result_payload = m.get('resultPayload')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

