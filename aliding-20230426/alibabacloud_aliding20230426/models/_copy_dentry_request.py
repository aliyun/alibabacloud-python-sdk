# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CopyDentryRequest(DaraModel):
    def __init__(
        self,
        dentry_id: str = None,
        name: str = None,
        space_id: str = None,
        target_space_id: str = None,
        tenant_context: main_models.CopyDentryRequestTenantContext = None,
        to_next_dentry_id: str = None,
        to_parent_dentry_id: str = None,
        to_prev_dentry_id: str = None,
    ):
        # This parameter is required.
        self.dentry_id = dentry_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.space_id = space_id
        # This parameter is required.
        self.target_space_id = target_space_id
        self.tenant_context = tenant_context
        self.to_next_dentry_id = to_next_dentry_id
        self.to_parent_dentry_id = to_parent_dentry_id
        self.to_prev_dentry_id = to_prev_dentry_id

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

        if self.name is not None:
            result['Name'] = self.name

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.target_space_id is not None:
            result['TargetSpaceId'] = self.target_space_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.to_next_dentry_id is not None:
            result['ToNextDentryId'] = self.to_next_dentry_id

        if self.to_parent_dentry_id is not None:
            result['ToParentDentryId'] = self.to_parent_dentry_id

        if self.to_prev_dentry_id is not None:
            result['ToPrevDentryId'] = self.to_prev_dentry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryId') is not None:
            self.dentry_id = m.get('DentryId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TargetSpaceId') is not None:
            self.target_space_id = m.get('TargetSpaceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.CopyDentryRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('ToNextDentryId') is not None:
            self.to_next_dentry_id = m.get('ToNextDentryId')

        if m.get('ToParentDentryId') is not None:
            self.to_parent_dentry_id = m.get('ToParentDentryId')

        if m.get('ToPrevDentryId') is not None:
            self.to_prev_dentry_id = m.get('ToPrevDentryId')

        return self

class CopyDentryRequestTenantContext(DaraModel):
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

