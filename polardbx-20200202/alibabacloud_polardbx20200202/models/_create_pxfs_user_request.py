# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePxfsUserRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        identity_name: str = None,
        posix_gid: int = None,
        posix_uid: int = None,
        region_id: str = None,
        role: str = None,
        tenant_id: str = None,
    ):
        # The PolarDB-X instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The name of the identity.
        # 
        # This parameter is required.
        self.identity_name = identity_name
        # POSIX GID
        # 
        # This parameter is required.
        self.posix_gid = posix_gid
        # POSIX UID
        # 
        # This parameter is required.
        self.posix_uid = posix_uid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The role of the identity.
        # 
        # This parameter is required.
        self.role = role
        # The ID of the tenant.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name

        if self.posix_gid is not None:
            result['PosixGid'] = self.posix_gid

        if self.posix_uid is not None:
            result['PosixUid'] = self.posix_uid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role is not None:
            result['Role'] = self.role

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')

        if m.get('PosixGid') is not None:
            self.posix_gid = m.get('PosixGid')

        if m.get('PosixUid') is not None:
            self.posix_uid = m.get('PosixUid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

