# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetUserDocumentPermissionRequest(DaraModel):
    def __init__(
        self,
        dentry_id: int = None,
        dentry_uuid: str = None,
        resource_type: int = None,
        space_id: int = None,
        tenant_context: main_models.GetUserDocumentPermissionRequestTenantContext = None,
    ):
        self.dentry_id = dentry_id
        self.dentry_uuid = dentry_uuid
        # This parameter is required.
        self.resource_type = resource_type
        self.space_id = space_id
        self.tenant_context = tenant_context

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

        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryId') is not None:
            self.dentry_id = m.get('DentryId')

        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.GetUserDocumentPermissionRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class GetUserDocumentPermissionRequestTenantContext(DaraModel):
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

