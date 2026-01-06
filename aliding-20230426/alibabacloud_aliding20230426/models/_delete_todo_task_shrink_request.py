# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTodoTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        operator_id: str = None,
        task_id: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.operator_id = operator_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

