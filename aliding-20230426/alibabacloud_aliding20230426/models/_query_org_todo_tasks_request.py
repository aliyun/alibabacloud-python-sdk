# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryOrgTodoTasksRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.QueryOrgTodoTasksRequestTenantContext = None,
        is_done: bool = None,
        next_token: str = None,
    ):
        self.tenant_context = tenant_context
        self.is_done = is_done
        self.next_token = next_token

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

        if self.is_done is not None:
            result['isDone'] = self.is_done

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.QueryOrgTodoTasksRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

class QueryOrgTodoTasksRequestTenantContext(DaraModel):
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

