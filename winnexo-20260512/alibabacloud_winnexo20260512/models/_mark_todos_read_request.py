# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MarkTodosReadRequest(DaraModel):
    def __init__(
        self,
        mark_all_read: bool = None,
        tenant_id: str = None,
        todo_ids: List[str] = None,
    ):
        # Specifies whether to mark all to-do items as read. This parameter takes precedence over the todoIds parameter.
        self.mark_all_read = mark_all_read
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The list of to-do item IDs. You can specify up to 100 IDs. This parameter is ignored if markAllRead is set to true.
        self.todo_ids = todo_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mark_all_read is not None:
            result['markAllRead'] = self.mark_all_read

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.todo_ids is not None:
            result['todoIds'] = self.todo_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('markAllRead') is not None:
            self.mark_all_read = m.get('markAllRead')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('todoIds') is not None:
            self.todo_ids = m.get('todoIds')

        return self

