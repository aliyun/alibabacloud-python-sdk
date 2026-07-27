# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLakebaseTenantTokenRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        polar_fs_instance_id: str = None,
        subdir: str = None,
        tenant: str = None,
    ):
        # The associated PolarDB instance ID.
        self.dbcluster_id = dbcluster_id
        # The PolarFS instance ID.
        # 
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The mount subdirectory. Specify an absolute path.
        # 
        # This parameter is required.
        self.subdir = subdir
        # The tenant identifier.
        self.tenant = tenant

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.subdir is not None:
            result['Subdir'] = self.subdir

        if self.tenant is not None:
            result['Tenant'] = self.tenant

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('Subdir') is not None:
            self.subdir = m.get('Subdir')

        if m.get('Tenant') is not None:
            self.tenant = m.get('Tenant')

        return self

