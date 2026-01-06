# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocBlocksModifyShrinkRequest(DaraModel):
    def __init__(
        self,
        block_id: str = None,
        dentry_uuid: str = None,
        element_shrink: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.block_id = block_id
        # This parameter is required.
        self.dentry_uuid = dentry_uuid
        # This parameter is required.
        self.element_shrink = element_shrink
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_id is not None:
            result['BlockId'] = self.block_id

        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.element_shrink is not None:
            result['Element'] = self.element_shrink

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockId') is not None:
            self.block_id = m.get('BlockId')

        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('Element') is not None:
            self.element_shrink = m.get('Element')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

