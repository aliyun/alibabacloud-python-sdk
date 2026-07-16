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
        # The Serverless cache storage capacity. Unit: GB.
        # > This parameter is required only for Serverless Pro instances.
        self.cache_storage_size = cache_storage_size
        # This parameter is deprecated. You do not need to specify this parameter.
        self.dbinstance_class = dbinstance_class
        # This parameter is deprecated. You do not need to specify this parameter.
        self.dbinstance_group_count = dbinstance_group_count
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in the specified region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The specifications of segment nodes. For information about supported node specifications, see [Instance specifications](https://help.aliyun.com/document_detail/35406.html).
        # 
        # > This parameter is supported only for elastic storage mode instances.
        self.instance_spec = instance_spec
        # This parameter is deprecated. You do not need to specify this parameter.
        self.master_node_num = master_node_num
        self.owner_id = owner_id
        # This parameter is deprecated. You do not need to specify this parameter.
        self.pay_type = pay_type
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query available region IDs.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. For information about how to obtain the resource group ID, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The performance level (PL) of the cloud disk. Valid values:
        # 
        # - **pl0**: PL0.
        # - **pl1**: PL1.
        # - **pl2**: PL2.
        self.seg_disk_performance_level = seg_disk_performance_level
        # The number of segment nodes. The supported number of nodes varies based on the instance resource type and instance edition:
        # 
        # - Elastic storage mode, High-availability Edition: Valid values: 4 to 512. The value must be a multiple of 4.
        # - Elastic storage mode, <props="china">Basic Edition (formerly High-performance Edition)<props="intl">High-performance Edition: Valid values: 2 to 512. The value must be a multiple of 2.
        # - Serverless manual scheduling mode: Valid values: 2 to 512. The value must be a multiple of 2.
        self.seg_node_num = seg_node_num
        # The cloud disk storage type after the change. Currently, only ESSD cloud disks are supported. Set the value to **cloud_essd**.
        self.seg_storage_type = seg_storage_type
        # - Serverless instances:
        # The compute resource threshold. Valid values: 8 to 32. The value must be a multiple of 8. Unit: ACU. Default value: 32.
        # 
        # - Serverless Pro instances: The reserved compute resources. Valid values: 16 to 1024. Unit: ACU. Default value: 16. The step size varies based on the value range:
        #   - 16 to 32: step size of 4.
        #   - 32 to 64: step size of 8.
        #   - 64 to 128: step size of 16.
        #   - 128 to 256: step size of 32.
        #   - Greater than 256: step size of 64.
        # > This parameter is required only for Serverless automatic scheduling mode and Serverless Pro instances.
        self.serverless_resource = serverless_resource
        # The storage capacity of segment nodes. Unit: GB. Valid values: 50 to <props="china">8000<props="intl">6000. The value must be a multiple of 50.
        # 
        # > This parameter is supported only for elastic storage mode instances.
        self.storage_size = storage_size
        # The type of the specification change. Valid values:
        # 
        # - **0** (default): Changes the number of segment nodes. SegNodeNum is required. Other parameters do not take effect.
        # - **1**: Changes the segment node specifications and instance storage capacity. InstanceSpec is required. StorageSize is optional and must be greater than or equal to the current instance storage capacity.
        # - **2**: Changes the number of master nodes. MasterNodeNum is required. Other parameters do not take effect.
        # - **3**: Changes the cloud disk storage type and performance level (PL). SegDiskPerformanceLevel and SegStorageType are required. Other parameters do not take effect.
        # 
        # > - Different instance resource types support different Upgrade/Downgrade operations for compute nodes. For more information, see [Precautions](https://help.aliyun.com/document_detail/50956.html).
        # - After you select a specification change type, only the corresponding parameters take effect. Other parameters do not take effect. For example, if **UpgradeType** is set to 0 and you specify both the number of segment nodes and the number of master nodes, only the number of segment nodes is changed.
        # - Changing the number of master nodes is supported only on the China site (aliyun.com).
        # - You can change the cloud disk storage type only from standard SSD to ESSD cloud disk.
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

