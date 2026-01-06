# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UnsubscribeEventRequest(DaraModel):
    def __init__(
        self,
        scope: str = None,
        scope_id: str = None,
        tenant_context: main_models.UnsubscribeEventRequestTenantContext = None,
    ):
        # This parameter is required.
        self.scope = scope
        # This parameter is required.
        self.scope_id = scope_id
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scope is not None:
            result['Scope'] = self.scope

        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.UnsubscribeEventRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class UnsubscribeEventRequestTenantContext(DaraModel):
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

