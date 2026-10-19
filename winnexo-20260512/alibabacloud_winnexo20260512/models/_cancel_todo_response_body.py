# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelTodoResponseBody(DaraModel):
    def __init__(
        self,
        cancelled_count: int = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        todo_id: str = None,
    ):
        # 作废条数
        self.cancelled_count = cancelled_count
        # 业务状态码；成功为200
        self.code = code
        # 错误描述
        self.message = message
        # 请求追踪ID
        self.request_id = request_id
        # 作废后状态
        self.status = status
        # 作废的待办ID（按 workItemId 定位时为空）
        self.todo_id = todo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelled_count is not None:
            result['cancelledCount'] = self.cancelled_count

        if self.code is not None:
            result['code'] = self.code

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
        if m.get('cancelledCount') is not None:
            self.cancelled_count = m.get('cancelledCount')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

