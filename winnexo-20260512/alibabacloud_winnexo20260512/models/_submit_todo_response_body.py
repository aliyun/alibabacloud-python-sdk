# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTodoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        completed_at: str = None,
        completed_by_user_id: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        todo_id: str = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 完成时间（ISO8601 UTC；与其他北京时间格式化字段格式不同）
        self.completed_at = completed_at
        # 完成人用户ID
        self.completed_by_user_id = completed_by_user_id
        # 错误描述
        self.message = message
        # 请求追踪ID
        self.request_id = request_id
        # 提交后状态（恒为 COMPLETED）
        self.status = status
        # 待办ID
        self.todo_id = todo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.completed_by_user_id is not None:
            result['completedByUserId'] = self.completed_by_user_id

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('completedByUserId') is not None:
            self.completed_by_user_id = m.get('completedByUserId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

