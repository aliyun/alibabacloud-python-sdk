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
        # The allowed permissions for the shared dataset. When a user accesses the shared dataset, their permissions are limited to this list. The default value is \\`["RO"]\\`.
        # 
        # - RO: Read-only permission. The recipient can only read the dataset.
        # 
        # - RW: Read and write permission. The recipient can read and modify the dataset.
        self.allowed_mount_access_levels = allowed_mount_access_levels
        # The expiration time. The time is in ISO 8601 format.
        # 
        # > If you do not specify this parameter, the sharing relationship never expires.
        self.expires_at = expires_at
        # Additional configurations for the sharing relationship. This parameter is a JSON string.
        # 
        # - AllowExportModel: Specifies whether to allow the export of trained models.
        # 
        # - AllowAccessDLCWebTerminal: Specifies whether to allow users to log on to the container in a DLC task.
        # 
        # - AllowAccessDLCFullLog: Specifies whether to allow access to the full task logs.
        self.extra = extra
        # Specifies whether to enable security protection for the shared dataset.
        self.is_secure_mode = is_secure_mode
        # The time when the dataset was shared. The time is in ISO 8601 format.
        self.shared_at = shared_at
        # The ID of the tenant that owns the source dataset. The user who shares the dataset must be a workspace administrator or the root account.
        self.source_tenant_id = source_tenant_id
        # The ID of the workspace that contains the source dataset.
        self.source_workspace_id = source_workspace_id
        # The status of the sharing relationship.
        # 
        # - ACTIVE: The sharing relationship is active. Complete dataset information is displayed only in this state.
        # 
        # - EXPIRED: The sharing relationship has expired.
        # 
        # - REVOKED: The sharing relationship was revoked by the sharer.
        # 
        # - INVALID: The sharing relationship is invalid. This can happen if the source dataset is deleted.
        self.status = status
        # The ID of the target tenant. This must be a root account ID.
        # 
        # > This parameter is required when you set a sharing relationship.
        self.tenant_id = tenant_id
        # The ID of the target workspace. This ID must be different from the source workspace ID.
        # 
        # > This parameter is required when you set a sharing relationship.
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

