# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetOrgOrWebOpenDocContentTaskIdRequest(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        generate_cp: bool = None,
        scope_type: int = None,
        target_format: str = None,
        tenant_context: main_models.GetOrgOrWebOpenDocContentTaskIdRequestTenantContext = None,
    ):
        # This parameter is required.
        self.dentry_uuid = dentry_uuid
        self.generate_cp = generate_cp
        self.scope_type = scope_type
        self.target_format = target_format
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.generate_cp is not None:
            result['GenerateCp'] = self.generate_cp

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.target_format is not None:
            result['TargetFormat'] = self.target_format

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('GenerateCp') is not None:
            self.generate_cp = m.get('GenerateCp')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('TargetFormat') is not None:
            self.target_format = m.get('TargetFormat')

        if m.get('TenantContext') is not None:
            temp_model = main_models.GetOrgOrWebOpenDocContentTaskIdRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class GetOrgOrWebOpenDocContentTaskIdRequestTenantContext(DaraModel):
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

