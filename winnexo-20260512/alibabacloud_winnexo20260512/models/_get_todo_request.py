# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTodoRequest(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        tenant_id: str = None,
        todo_id: str = None,
        work_item_id: str = None,
    ):
        # assistant 消息ID（按消息反查多条）
        self.message_id = message_id
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 待办ID（单条查询）
        self.todo_id = todo_id
        # 工作项ID（按来源反查多条）
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

