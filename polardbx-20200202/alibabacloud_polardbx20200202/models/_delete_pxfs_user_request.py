# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePxfsUserRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        identity_name: str = None,
        region_id: str = None,
        tenant_id: str = None,
    ):
        # The PolarDB-X instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The identity name.
        # 
        # This parameter is required.
        self.identity_name = identity_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tenant ID.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

