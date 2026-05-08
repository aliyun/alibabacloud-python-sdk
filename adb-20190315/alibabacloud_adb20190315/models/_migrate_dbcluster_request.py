# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateDBClusterRequest(DaraModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_id: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        product_form: str = None,
        product_version: str = None,
        reserved_node_count: int = None,
        reserved_node_size: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secondary_vswitch_id: str = None,
        secondary_zone_id: str = None,
        shard_number: str = None,
        storage_resource: str = None,
        storage_resource_size: str = None,
    ):
        # The amount of reserved computing resources.
        # Valid values: 0ACU to 4096ACU. Step size: 16. Each AnalyticDB compute unit (ACU) is approximately equal to 1 core and 4 GB memory.
        self.compute_resource = compute_resource
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.product_form = product_form
        self.product_version = product_version
        self.reserved_node_count = reserved_node_count
        self.reserved_node_size = reserved_node_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secondary_vswitch_id = secondary_vswitch_id
        self.secondary_zone_id = secondary_zone_id
        # The number of shards that you want to change during the data migration.
        self.shard_number = shard_number
        # The amount of reserved storage resources. Valid values: 0ACU to 2064ACU. The value must be in increments of the number of ACUs specified by the StorageResourceSize parameter × 3 (default value: 24ACU). Each ACU is approximately equal to 1 core and 4 GB memory.
        # 
        # >  This parameter must be specified with a unit.
        self.storage_resource = storage_resource
        # The node specifications of reserved storage resources. Valid values: 8ACU, 12ACU, and 16ACU.
        self.storage_resource_size = storage_resource_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_form is not None:
            result['ProductForm'] = self.product_form

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.reserved_node_count is not None:
            result['ReservedNodeCount'] = self.reserved_node_count

        if self.reserved_node_size is not None:
            result['ReservedNodeSize'] = self.reserved_node_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secondary_vswitch_id is not None:
            result['SecondaryVSwitchId'] = self.secondary_vswitch_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.shard_number is not None:
            result['ShardNumber'] = self.shard_number

        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource

        if self.storage_resource_size is not None:
            result['StorageResourceSize'] = self.storage_resource_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductForm') is not None:
            self.product_form = m.get('ProductForm')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('ReservedNodeCount') is not None:
            self.reserved_node_count = m.get('ReservedNodeCount')

        if m.get('ReservedNodeSize') is not None:
            self.reserved_node_size = m.get('ReservedNodeSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecondaryVSwitchId') is not None:
            self.secondary_vswitch_id = m.get('SecondaryVSwitchId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('ShardNumber') is not None:
            self.shard_number = m.get('ShardNumber')

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        if m.get('StorageResourceSize') is not None:
            self.storage_resource_size = m.get('StorageResourceSize')

        return self

