# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DatasetShareRelationship(DaraModel):
    def __init__(
        self,
        allowed_mount_access_levels: List[str] = None,
        expires_at: str = None,
        extra: str = None,
        is_secure_mode: bool = None,
        shared_at: str = None,
        source_tenant_id: str = None,
        source_workspace_id: str = None,
        status: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.allowed_mount_access_levels = allowed_mount_access_levels
        self.expires_at = expires_at
        self.extra = extra
        self.is_secure_mode = is_secure_mode
        self.shared_at = shared_at
        self.source_tenant_id = source_tenant_id
        self.source_workspace_id = source_workspace_id
        self.status = status
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_mount_access_levels is not None:
            result['AllowedMountAccessLevels'] = self.allowed_mount_access_levels

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.is_secure_mode is not None:
            result['IsSecureMode'] = self.is_secure_mode

        if self.shared_at is not None:
            result['SharedAt'] = self.shared_at

        if self.source_tenant_id is not None:
            result['SourceTenantId'] = self.source_tenant_id

        if self.source_workspace_id is not None:
            result['SourceWorkspaceId'] = self.source_workspace_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedMountAccessLevels') is not None:
            self.allowed_mount_access_levels = m.get('AllowedMountAccessLevels')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('IsSecureMode') is not None:
            self.is_secure_mode = m.get('IsSecureMode')

        if m.get('SharedAt') is not None:
            self.shared_at = m.get('SharedAt')

        if m.get('SourceTenantId') is not None:
            self.source_tenant_id = m.get('SourceTenantId')

        if m.get('SourceWorkspaceId') is not None:
            self.source_workspace_id = m.get('SourceWorkspaceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

