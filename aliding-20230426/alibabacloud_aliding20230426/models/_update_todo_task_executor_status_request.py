# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdateTodoTaskExecutorStatusRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.UpdateTodoTaskExecutorStatusRequestTenantContext = None,
        executor_status_list: List[main_models.UpdateTodoTaskExecutorStatusRequestExecutorStatusList] = None,
        operator_id: str = None,
        task_id: str = None,
    ):
        self.tenant_context = tenant_context
        self.executor_status_list = executor_status_list
        self.operator_id = operator_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()
        if self.executor_status_list:
            for v1 in self.executor_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        result['executorStatusList'] = []
        if self.executor_status_list is not None:
            for k1 in self.executor_status_list:
                result['executorStatusList'].append(k1.to_map() if k1 else None)

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdateTodoTaskExecutorStatusRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        self.executor_status_list = []
        if m.get('executorStatusList') is not None:
            for k1 in m.get('executorStatusList'):
                temp_model = main_models.UpdateTodoTaskExecutorStatusRequestExecutorStatusList()
                self.executor_status_list.append(temp_model.from_map(k1))

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class UpdateTodoTaskExecutorStatusRequestExecutorStatusList(DaraModel):
    def __init__(
        self,
        id: str = None,
        is_done: bool = None,
    ):
        self.id = id
        self.is_done = is_done

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.is_done is not None:
            result['isDone'] = self.is_done

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')

        return self

class UpdateTodoTaskExecutorStatusRequestTenantContext(DaraModel):
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

