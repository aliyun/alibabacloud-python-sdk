# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgenticDBTenantRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        description: str = None,
        region_id: str = None,
        tenant_name: str = None,
    ):
        # The AgenticDB cluster ID, which starts with pagc-. You can obtain this ID after creating a cluster by calling CreateDBCluster with AgenticDbType set to dedicated. Standard PolarDB cluster IDs start with pc- and are not supported by this operation.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The tenant description. The description can be up to 256 characters in length.
        self.description = description
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tenant name.
        # 
        # This parameter is required.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        return self

