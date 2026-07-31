# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RedeployDedicatedHostRequest(DaraModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        migration_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the dedicated host.
        # 
        # This parameter is required.
        self.dedicated_host_id = dedicated_host_id
        # Specifies whether to stop ECS instance before migrating it to the destination dedicated host. Valid values:
        # 
        # - Reboot: stops ECS instance before migration.
        # 
        # - LiveMigrationFirst: migrates ECS instance without stopping it. You must specify the DedicatedHostId parameter. This value does not support changing ECS instance type during migration. If live migration fails, cold migration is performed by default.
        # 
        # Default value: Reboot.
        self.migration_type = migration_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the dedicated host. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

