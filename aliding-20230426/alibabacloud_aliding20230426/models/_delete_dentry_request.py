# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class DeleteDentryRequest(DaraModel):
    def __init__(
        self,
        dentry_id: str = None,
        space_id: str = None,
        tenant_context: main_models.DeleteDentryRequestTenantContext = None,
        to_recycle_bin: bool = None,
    ):
        # This parameter is required.
        self.dentry_id = dentry_id
        # This parameter is required.
        self.space_id = space_id
        self.tenant_context = tenant_context
        self.to_recycle_bin = to_recycle_bin

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_id is not None:
            result['DentryId'] = self.dentry_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.to_recycle_bin is not None:
            result['ToRecycleBin'] = self.to_recycle_bin

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryId') is not None:
            self.dentry_id = m.get('DentryId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.DeleteDentryRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('ToRecycleBin') is not None:
            self.to_recycle_bin = m.get('ToRecycleBin')

        return self

class DeleteDentryRequestTenantContext(DaraModel):
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

