# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class DeleteTodoTaskRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.DeleteTodoTaskRequestTenantContext = None,
        operator_id: str = None,
        task_id: str = None,
    ):
        self.tenant_context = tenant_context
        self.operator_id = operator_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.DeleteTodoTaskRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class DeleteTodoTaskRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

