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
        self.cache_storage_size = cache_storage_size
        # This parameter is no longer used.
        self.dbinstance_class = dbinstance_class
        # This parameter is no longer used.
        self.dbinstance_group_count = dbinstance_group_count
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The specifications of each compute node. For information about the supported specifications, see [Instance specifications](https://help.aliyun.com/document_detail/35406.html).
        # 
        # > This parameter is available only for instances in elastic storage mode.
        self.instance_spec = instance_spec
        # This parameter is no longer used.
        self.master_node_num = master_node_num
        self.owner_id = owner_id
        # This parameter is no longer used.
        self.pay_type = pay_type
        # The region ID of the instance.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The performance level of Enterprise SSDs (ESSDs). Valid values:
        # 
        # *   **pl0**
        # *   **pl1**
        # *   **pl2**
        self.seg_disk_performance_level = seg_disk_performance_level
        # The number of compute nodes. The number of compute nodes varies based on the instance resource type and edition.
        # 
        # *   Valid values for High-availability Edition instances in elastic storage mode: 4 to 512, in 4 increments.
        # *   Valid values for High-performance Edition instances in elastic storage mode: 2 to 512, in 2 increments.
        # *   Valid values for instances in manual Serverless mode: 2 to 512, in 2 increments.
        self.seg_node_num = seg_node_num
        # The disk storage type of the instance after the change. The disk storage type can be changed only to ESSD. Set the value to **cloud_essd**.
        self.seg_storage_type = seg_storage_type
        self.serverless_resource = serverless_resource
        # The storage capacity of each compute node. Unit: GB. Valid values: 50 to 6000, in 50 increments.
        # 
        # >  This parameter is available only for instances in elastic storage mode.
        self.storage_size = storage_size
        # The type of the instance configuration change. Valid values:
        # 
        # *   **0** (default): changes the number of compute nodes.
        # *   **1**: changes the specifications and storage capacity of each compute node.
        # *   **2**: changes the number of coordinator nodes.
        # *   **3**: changes the disk storage type and ESSD performance level of the instance.
        # 
        # > 
        # 
        # *   The supported changes to compute node configurations vary based on the instance resource type. For more information, see the "Usage notes" section of the [Change compute node configurations](https://help.aliyun.com/document_detail/50956.html) topic.
        # 
        # *   After you specify a change type, only the corresponding parameters take effect. For example, if you set **UpgradeType** to 0, the parameter that is used to change the number of compute nodes takes effect, but the parameter that is used to change the number of coordinator nodes does not.
        # *   The number of coordinator nodes can be changed only on the China site (aliyun.com).
        # *   The disk storage type can be changed only from ultra disks to ESSDs.
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

