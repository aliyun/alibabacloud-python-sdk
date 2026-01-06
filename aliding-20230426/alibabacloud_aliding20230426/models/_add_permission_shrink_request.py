# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPermissionShrinkRequest(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        members_shrink: str = None,
        option_shrink: str = None,
        role_id: str = None,
        tenant_context_shrink: str = None,
    ):
        self.dentry_uuid = dentry_uuid
        # This parameter is required.
        self.members_shrink = members_shrink
        self.option_shrink = option_shrink
        # This parameter is required.
        self.role_id = role_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.members_shrink is not None:
            result['Members'] = self.members_shrink

        if self.option_shrink is not None:
            result['Option'] = self.option_shrink

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')

        if m.get('Option') is not None:
            self.option_shrink = m.get('Option')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

