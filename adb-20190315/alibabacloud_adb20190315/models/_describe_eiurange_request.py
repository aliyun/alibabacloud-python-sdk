# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEIURangeRequest(DaraModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_id: str = None,
        dbcluster_version: str = None,
        operation: str = None,
        owner_account: str = None,
        owner_id: int = None,
        product_version: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_size: str = None,
        sub_operation: str = None,
        zone_id: str = None,
    ):
        # The specifications of computing resources.
        # 
        # >  You can call the [DescribeComputeResource](https://help.aliyun.com/document_detail/469002.html) operation to query the specifications of computing resources.
        self.compute_resource = compute_resource
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # *   This parameter can be left empty when **Operation** is set to **Buy**.
        # *   This parameter must be specified when **Operation** is set to **Upgrade** or **Downgrade**.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The version of the AnalyticDB for MySQL Data Warehouse Edition cluster. Set the value to **3.0**.
        self.dbcluster_version = dbcluster_version
        # The type of the operation. Valid values:
        # 
        # *   **Buy**: purchases a cluster.
        # *   **Modify**: changes configurations of a cluster.
        self.operation = operation
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.product_version = product_version
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The specifications of storage resources. Default value: **8ACU**. Valid values:
        # 
        # *   **8ACU**
        # *   **12ACU**
        # *   **16ACU**
        self.storage_size = storage_size
        # The type of the sub-operation. Valid values:
        # 
        # *   **Upgrade**: upgrades a cluster.
        # *   **Downgrade**: downgrades a cluster.
        self.sub_operation = sub_operation
        # The zone ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/612293.html) operation to query the most recent zone list.
        self.zone_id = zone_id

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

        if self.dbcluster_version is not None:
            result['DBClusterVersion'] = self.dbcluster_version

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.sub_operation is not None:
            result['SubOperation'] = self.sub_operation

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBClusterVersion') is not None:
            self.dbcluster_version = m.get('DBClusterVersion')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('SubOperation') is not None:
            self.sub_operation = m.get('SubOperation')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

