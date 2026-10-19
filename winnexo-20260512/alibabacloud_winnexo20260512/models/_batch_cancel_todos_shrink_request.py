# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchCancelTodosShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
        todo_ids_shrink: str = None,
    ):
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 待办ID列表（1~100）
        # 
        # This parameter is required.
        self.todo_ids_shrink = todo_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.todo_ids_shrink is not None:
            result['todoIds'] = self.todo_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('todoIds') is not None:
            self.todo_ids_shrink = m.get('todoIds')

        return self

