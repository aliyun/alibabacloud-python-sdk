# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDentryShrinkRequest(DaraModel):
    def __init__(
        self,
        dentry_id: str = None,
        space_id: str = None,
        tenant_context_shrink: str = None,
        to_recycle_bin: bool = None,
    ):
        # This parameter is required.
        self.dentry_id = dentry_id
        # This parameter is required.
        self.space_id = space_id
        self.tenant_context_shrink = tenant_context_shrink
        self.to_recycle_bin = to_recycle_bin

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_id is not None:
            result['DentryId'] = self.dentry_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

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
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('ToRecycleBin') is not None:
            self.to_recycle_bin = m.get('ToRecycleBin')

        return self

