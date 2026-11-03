# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgenticDBTenantApiKeyRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        description: str = None,
        expire_time: str = None,
        region_id: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
    ):
        # The AgenticDB cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The usage description.
        self.description = description
        # The expiration time in ISO 8601 format. If this parameter is not specified, the API key never expires.
        self.expire_time = expire_time
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies the ID of an existing tenant. If you specify this parameter, an API key is created only for the existing tenant in the current cluster. If the tenant does not exist, an error is returned and no tenant is created. If TenantName is also specified, the name must match the name of the tenant.
        self.tenant_id = tenant_id
        # The name of the tenant. The name must be unique within the cluster and must be 2 to 64 characters in length.
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        return self

