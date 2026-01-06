# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class DocBlocksModifyRequest(DaraModel):
    def __init__(
        self,
        block_id: str = None,
        dentry_uuid: str = None,
        element: Dict[str, Any] = None,
        tenant_context: main_models.DocBlocksModifyRequestTenantContext = None,
    ):
        # This parameter is required.
        self.block_id = block_id
        # This parameter is required.
        self.dentry_uuid = dentry_uuid
        # This parameter is required.
        self.element = element
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_id is not None:
            result['BlockId'] = self.block_id

        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.element is not None:
            result['Element'] = self.element

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')

        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('Element') is not None:
            self.element = m.get('Element')

        if m.get('TenantContext') is not None:
            temp_model = main_models.DocBlocksModifyRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class DocBlocksModifyRequestTenantContext(DaraModel):
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

