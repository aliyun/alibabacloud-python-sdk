# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBInstanceRequest(DaraModel):
    def __init__(
        self,
        cache_storage_size: str = None,
        dbinstance_class: str = None,
        dbinstance_group_count: str = None,
        dbinstance_id: str = None,
        instance_spec: str = None,
        master_node_num: str = None,
        owner_id: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        seg_disk_performance_level: str = None,
        seg_node_num: str = None,
        seg_storage_type: str = None,
        serverless_resource: str = None,
        storage_size: str = None,
        upgrade_type: int = None,
    ):
        # Specifies the cache storage for Serverless Pro instances. Unit: GB.
        # 
        # > This parameter is required only for Serverless Pro instances.
        self.cache_storage_size = cache_storage_size
        # This parameter is deprecated.
        self.dbinstance_class = dbinstance_class
        # This parameter is deprecated.
        self.dbinstance_group_count = dbinstance_group_count
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in the specified region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The specifications of segment nodes. For supported node specifications, see [Instance types](https://help.aliyun.com/document_detail/35406.html).
        # 
        # > This parameter is available only for instances in storage-elastic mode.
        self.instance_spec = instance_spec
        # The number of master nodes.
        self.master_node_num = master_node_num
        self.owner_id = owner_id
        # This parameter is deprecated.
        self.pay_type = pay_type
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query available region IDs.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. To obtain the resource group ID, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The performance level (PL) of the disk. Valid values:
        # 
        # - **pl0**: PL0.
        # 
        # - **pl1**: PL1.
        # 
        # - **pl2**: PL2.
        self.seg_disk_performance_level = seg_disk_performance_level
        # The number of segment nodes. The supported number of nodes varies based on the instance resource type and edition:
        # 
        # - Instances in storage-elastic mode (High-availability Edition): 4 to 512, in increments of 4.
        # 
        # - Instances in storage-elastic mode (High-performance Edition): 2 to 512, in increments of 2.
        # 
        # - Instances in Serverless manual-scheduling mode: 2 to 512, in increments of 2.
        self.seg_node_num = seg_node_num
        # The new disk storage type. You can only upgrade to an ESSD cloud disk. To do so, set this parameter to **cloud_essd**.
        self.seg_storage_type = seg_storage_type
        # - For an instance in Serverless automatic-scheduling mode, this parameter specifies the computing resource threshold. The value must be a multiple of 8 in the range of 8 to 32. Unit: ACU. Default value: 32.
        # 
        # - For a Serverless Pro instance, this parameter specifies the reserved computing resources. Valid values range from 16 to 1,024. Unit: ACU. Default value: 16. Increment rules:
        # 
        #   - 16 to 32: in increments of 4.
        # 
        #   - 32 to 64: in increments of 8.
        # 
        #   - 64 to 128: in increments of 16.
        # 
        #   - 128 to 256: in increments of 32.
        # 
        #   - Greater than 256: in increments of 64.
        # 
        # > This parameter is required only for instances in Serverless automatic-scheduling mode and Serverless Pro instances.
        self.serverless_resource = serverless_resource
        # The storage capacity of each segment node. Unit: GB. The value must be a multiple of 50 in the range of 50 to <props="china">8,000<props="intl">6,000.
        # 
        # > This parameter is available only for instances in storage-elastic mode.
        self.storage_size = storage_size
        # The type of specification change. Valid values:
        # 
        # - **0** (default): Changes the number of segment nodes. The SegNodeNum parameter is required, and other parameters are ignored.
        # 
        # - **1**: Changes the specifications and storage capacity of segment nodes. The InstanceSpec parameter is required. The StorageSize parameter is optional. If specified, its value must be greater than or equal to the current storage capacity of the instance.
        # 
        # - **2**: Changes the number of master nodes. The MasterNodeNum parameter is required, and other parameters are ignored.
        # 
        # - **3**: Changes the disk storage type and performance level. The SegDiskPerformanceLevel and SegStorageType parameters are required, and other parameters are ignored.
        # 
        # > * Support for scaling computing resources varies by instance resource type. For more information, see [Usage notes](https://help.aliyun.com/document_detail/50956.html).
        # 
        # - If you select a change type, only the parameters associated with that type take effect; other parameters are ignored. For example, if you set **UpgradeType** to 0 and specify parameters to change both the number of segment nodes and the number of master nodes, only the parameters for changing the number of segment nodes take effect.
        # 
        # - You can change the number of master nodes only on the Alibaba Cloud China site.
        # 
        # - You can change the disk storage type only from ultra disk to ESSD cloud disk.
        self.upgrade_type = upgrade_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_storage_size is not None:
            result['CacheStorageSize'] = self.cache_storage_size

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_group_count is not None:
            result['DBInstanceGroupCount'] = self.dbinstance_group_count

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.master_node_num is not None:
            result['MasterNodeNum'] = self.master_node_num

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.seg_disk_performance_level is not None:
            result['SegDiskPerformanceLevel'] = self.seg_disk_performance_level

        if self.seg_node_num is not None:
            result['SegNodeNum'] = self.seg_node_num

        if self.seg_storage_type is not None:
            result['SegStorageType'] = self.seg_storage_type

        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheStorageSize') is not None:
            self.cache_storage_size = m.get('CacheStorageSize')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceGroupCount') is not None:
            self.dbinstance_group_count = m.get('DBInstanceGroupCount')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('MasterNodeNum') is not None:
            self.master_node_num = m.get('MasterNodeNum')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SegDiskPerformanceLevel') is not None:
            self.seg_disk_performance_level = m.get('SegDiskPerformanceLevel')

        if m.get('SegNodeNum') is not None:
            self.seg_node_num = m.get('SegNodeNum')

        if m.get('SegStorageType') is not None:
            self.seg_storage_type = m.get('SegStorageType')

        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        return self

