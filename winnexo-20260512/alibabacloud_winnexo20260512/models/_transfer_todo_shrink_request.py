# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferTodoShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        target_user_ids_shrink: str = None,
        tenant_id: str = None,
        todo_id: str = None,
    ):
        # The handover description.
        self.comment = comment
        # The list of target user IDs to whom the task is reassigned. You can specify 1 to 100 user IDs.
        # 
        # This parameter is required.
        self.target_user_ids_shrink = target_user_ids_shrink
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The ID of the to-do task.
        # 
        # This parameter is required.
        self.todo_id = todo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.target_user_ids_shrink is not None:
            result['targetUserIds'] = self.target_user_ids_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('targetUserIds') is not None:
            self.target_user_ids_shrink = m.get('targetUserIds')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

