# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelTodoRequest(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
        todo_id: str = None,
        work_item_id: str = None,
    ):
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The ID of the to-do item. You must specify either this parameter or workItemId.
        self.todo_id = todo_id
        # The ID of the work item. You can use this parameter to cancel to-do items in batches by source. You must specify either this parameter or todoId.
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

