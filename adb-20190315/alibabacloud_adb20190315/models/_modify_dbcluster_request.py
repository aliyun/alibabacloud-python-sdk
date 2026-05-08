# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterRequest(DaraModel):
    def __init__(
        self,
        compute_resource: str = None,
        dbcluster_category: str = None,
        dbcluster_id: str = None,
        dbnode_class: str = None,
        dbnode_group_count: str = None,
        dbnode_storage: str = None,
        disk_performance_level: str = None,
        elastic_ioresource: int = None,
        elastic_ioresource_size: str = None,
        executor_count: str = None,
        mode: str = None,
        modify_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_resource: str = None,
    ):
        # The computing resources of the cluster. You can call the [DescribeAvailableResource](https://help.aliyun.com/document_detail/190632.html) operation to query the computing resources that are available within a region.
        # 
        # > This parameter must be specified when Mode is set to Flexible.
        self.compute_resource = compute_resource
        # The edition of the cluster. Valid values:
        # 
        # *   **Cluster**: reserved mode for Cluster Edition.
        # *   **MixedStorage**: elastic mode for Cluster Edition.
        # 
        # > If you set DBClusterCategory to Cluster, you must set Mode to Reserver. If you set DBClusterCategory to MixedStorage, you must set Mode to Flexible. Otherwise, you fail to change the specifications of the cluster.
        self.dbcluster_category = dbcluster_category
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The node specifications of the cluster. Valid values:
        # 
        # *   **C8**
        # *   **C32**
        # 
        # > This parameter must be specified when Mode is set to Reserver.
        self.dbnode_class = dbnode_class
        # The number of node groups. Valid values: 1 to 200.
        # 
        # > This parameter must be specified when Mode is set to Reserver.
        self.dbnode_group_count = dbnode_group_count
        # The storage capacity per node. Unit: GB.
        # 
        # *   Valid values when DBClusterClass is set to C8: 100 to 2000.
        # *   Valid values when DBClusterClass is set to C32: 100 to 8000.
        # 
        # > 
        # 
        # *   This parameter must be specified when Mode is set to Reserver.
        # 
        # *   The storage capacity less than 1,000 GB increases in 100 GB increments. The storage capacity greater than 1,000 GB increases in 1,000 GB increments.
        self.dbnode_storage = dbnode_storage
        # The Enterprise SSD (ESSD) performance level of the cluster. Valid values:
        # 
        # *   PL0
        # *   PL1
        # *   PL2
        # *   PL3
        self.disk_performance_level = disk_performance_level
        # The number of EIUs. The number of EIUs that you can purchase varies based on the single-node EIU specifications.
        # 
        # *   If the single-node EIU specifications are 8 cores and 64 GB, you can purchase up to 32 EIUs.
        # *   If the single-node EIU specifications are 12 cores and 96 GB, you can purchase up to 16 EIUs.
        self.elastic_ioresource = elastic_ioresource
        # The single-node specifications of an elastic I/O unit (EIU). Valid values:
        # 
        # *   **8Core64GB**: If you set the parameter to **8Core64GB**, the specifications of an EIU are 24 cores and 192 GB memory.
        # *   **12Core96GB**: If you set the parameter to **12Core96GB**, the specifications of an EIU are 36 cores and 288 GB memory.
        # 
        # >  This parameter takes effect only when your cluster meets the following requirements:
        # 
        # *   The cluster is in elastic mode.
        # 
        # *   If the cluster resides in the China (Guangzhou), China (Shenzhen), China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), or China (Zhangjiakou) region, the cluster has 16 cores and 64 GB memory or higher specifications.
        # 
        # *   If the cluster resides in another region, the cluster has 32 cores and 128 GB memory or higher specifications.
        self.elastic_ioresource_size = elastic_ioresource_size
        # N/A
        self.executor_count = executor_count
        # The mode of the cluster. Valid values:
        # 
        # *   **Reserver**: the reserved mode.
        # *   **Flexible**: the elastic mode.
        self.mode = mode
        # The change type. Valid values:
        # 
        # *   **Upgrade**
        # *   **Downgrade**
        self.modify_type = modify_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the cluster. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # N/A
        self.storage_resource = storage_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource

        if self.dbcluster_category is not None:
            result['DBClusterCategory'] = self.dbcluster_category

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_group_count is not None:
            result['DBNodeGroupCount'] = self.dbnode_group_count

        if self.dbnode_storage is not None:
            result['DBNodeStorage'] = self.dbnode_storage

        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level

        if self.elastic_ioresource is not None:
            result['ElasticIOResource'] = self.elastic_ioresource

        if self.elastic_ioresource_size is not None:
            result['ElasticIOResourceSize'] = self.elastic_ioresource_size

        if self.executor_count is not None:
            result['ExecutorCount'] = self.executor_count

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

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

        if self.storage_resource is not None:
            result['StorageResource'] = self.storage_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResource') is not None:
            self.compute_resource = m.get('ComputeResource')

        if m.get('DBClusterCategory') is not None:
            self.dbcluster_category = m.get('DBClusterCategory')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeGroupCount') is not None:
            self.dbnode_group_count = m.get('DBNodeGroupCount')

        if m.get('DBNodeStorage') is not None:
            self.dbnode_storage = m.get('DBNodeStorage')

        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')

        if m.get('ElasticIOResource') is not None:
            self.elastic_ioresource = m.get('ElasticIOResource')

        if m.get('ElasticIOResourceSize') is not None:
            self.elastic_ioresource_size = m.get('ElasticIOResourceSize')

        if m.get('ExecutorCount') is not None:
            self.executor_count = m.get('ExecutorCount')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

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

        if m.get('StorageResource') is not None:
            self.storage_resource = m.get('StorageResource')

        return self

