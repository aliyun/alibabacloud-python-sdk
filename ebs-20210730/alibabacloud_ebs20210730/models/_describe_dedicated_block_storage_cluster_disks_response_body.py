# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedBlockStorageClusterDisksResponseBody(DaraModel):
    def __init__(
        self,
        disks: main_models.DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The collection of cloud disk information.
        self.disks = disks
        # The pagination token returned in this call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.disks:
            self.disks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disks is not None:
            result['Disks'] = self.disks.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disks') is not None:
            temp_model = main_models.DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks()
            self.disks = temp_model.from_map(m.get('Disks'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks(DaraModel):
    def __init__(
        self,
        disk: List[main_models.DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDisk] = None,
    ):
        # The collection of cloud disk information.
        self.disk = disk

    def validate(self):
        if self.disk:
            for v1 in self.disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Disk'] = []
        if self.disk is not None:
            for k1 in self.disk:
                result['Disk'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk = []
        if m.get('Disk') is not None:
            for k1 in m.get('Disk'):
                temp_model = main_models.DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDisk()
                self.disk.append(temp_model.from_map(k1))

        return self

class DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDisk(DaraModel):
    def __init__(
        self,
        attached_time: str = None,
        bdf_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        delete_auto_snapshot: bool = None,
        delete_with_instance: bool = None,
        description: str = None,
        detached_time: str = None,
        device: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_name: str = None,
        enable_auto_snapshot: bool = None,
        encrypted: bool = None,
        iops: int = None,
        image_id: str = None,
        instance_id: str = None,
        kmskey_id: str = None,
        mount_instance_num: int = None,
        multi_attach: str = None,
        performance_level: str = None,
        portable: bool = None,
        provisioned_iops: int = None,
        region_id: str = None,
        size: int = None,
        source_snapshot_id: str = None,
        status: str = None,
        storage_cluster_id: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        tags: List[main_models.DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDiskTags] = None,
        throughput: int = None,
        type: str = None,
        zone_id: str = None,
    ):
        # The time when the cloud disk was last attached. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddThh:mmZ format. The time is displayed in UTC.
        self.attached_time = attached_time
        # This parameter is in invitational preview and is not publicly available.
        self.bdf_id = bdf_id
        # Indicates whether the burst (performance burst) feature is enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # This parameter is supported only when `DiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The category of the cloud disk or local disk is cloud_essd, which indicates an ESSD.
        self.category = category
        # Indicates whether automatic snapshots are deleted when the cloud disk is released. Valid values:
        # 
        # - true: Automatic snapshots are deleted when the cloud disk is released.
        # - false: Automatic snapshots are retained when the cloud disk is released.
        # 
        # Snapshots created by calling [CreateSnapshot](https://help.aliyun.com/document_detail/25524.html) or by using the console are not affected by this parameter and are always retained.
        self.delete_auto_snapshot = delete_auto_snapshot
        # Indicates whether the cloud disk is released when the instance is released. Valid values:
        # 
        # - true: The cloud disk is released when the instance is released.
        # - false: The cloud disk is retained when the instance is released.
        self.delete_with_instance = delete_with_instance
        # The cloud disk description.
        self.description = description
        # The time when the cloud disk was last detached.
        self.detached_time = detached_time
        # The device name of the instance to which the cloud disk is attached, such as /dev/xvdb. Note the following items:
        # 
        # - This parameter has a value only when the `Status` parameter is set to `In_use`. This parameter is empty in other states.
        # 
        # - For cloud disks with the multi-attach feature enabled, this value is always empty. You can view all attachment information of the cloud disk from the returned `Attachment` list.
        # 
        # > This parameter will be deprecated. To ensure code compatibility, do not use this parameter.
        self.device = device
        # The billing method of the cloud disk. Valid values:
        # 
        # - PrePaid: subscription.
        # - PostPaid: pay-as-you-go.
        self.disk_charge_type = disk_charge_type
        # The cloud disk ID.
        self.disk_id = disk_id
        # The cloud disk name.
        self.disk_name = disk_name
        # Indicates whether the automatic snapshot policy feature is enabled for the cloud disk.
        # 
        # >This parameter is deprecated. After a cloud disk is created, the automatic snapshot policy feature is enabled by default. You only need to associate an automatic snapshot policy with the cloud disk.
        self.enable_auto_snapshot = enable_auto_snapshot
        # Indicates whether the cloud disk is encrypted.
        self.encrypted = encrypted
        # The maximum number of read/write (I/O) operations per second. Unit: operations/s.
        self.iops = iops
        # The ID of the image used to create the ECS instance. This parameter has a value only for cloud disks created from an image. Otherwise, this value is empty. This value remains unchanged throughout the lifecycle of the cloud disk.
        self.image_id = image_id
        # The instance ID of the instance to which the cloud disk is mounted. Note the following items:
        # 
        # - This parameter has a value only when the `Status` parameter is set to `In_use`. This parameter is empty in other states.
        # 
        # - For cloud disks with the multi-attach attribute enabled, this value is always empty. You can view all mount information of the cloud disk from the returned `Attachment` list.
        self.instance_id = instance_id
        # The KMS key ID used by the cloud disk.
        self.kmskey_id = kmskey_id
        # The number of instances to which the shared storage is attached.
        self.mount_instance_num = mount_instance_num
        # Indicates whether the multi-attach feature is enabled for the cloud disk.
        self.multi_attach = multi_attach
        # The performance level of the ESSD. Valid values:
        # 
        # - PL0: a maximum of 10,000 random read/write IOPS per cloud disk.
        # - PL1: a maximum of 50,000 random read/write IOPS per cloud disk.
        # - PL2: a maximum of 100,000 random read/write IOPS per cloud disk.
        # - PL3: a maximum of 1,000,000 random read/write IOPS per cloud disk.
        self.performance_level = performance_level
        # Indicates whether the cloud disk is removable.
        self.portable = portable
        # The provisioned read/write IOPS of the ESSD AutoPL cloud disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # This parameter is supported only when `DiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The region ID of the cloud disk.
        self.region_id = region_id
        # The cloud disk size. Unit: GiB.
        self.size = size
        # The ID of the snapshot used to create the cloud disk.
        # 
        # If no snapshot was specified when the cloud disk was created, this value is empty. This value remains unchanged throughout the lifecycle of the cloud disk.
        self.source_snapshot_id = source_snapshot_id
        # The cloud disk status. For more information, see [Cloud disk status](https://help.aliyun.com/document_detail/25689.html). Valid values:
        # 
        # -   In_use.
        # -   Available.
        # -   Attaching.
        # -   Detaching.
        # -   Creating.
        # -   ReIniting.
        self.status = status
        # The ID of the dedicated block storage cluster to which the cloud disk belongs. If the cloud disk belongs to a public cloud block storage cluster, this value is empty.
        self.storage_cluster_id = storage_cluster_id
        # The storage set ID.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set.
        self.storage_set_partition_number = storage_set_partition_number
        # The tags of the cloud disk.
        self.tags = tags
        # The amount of data that can be transferred per unit of time. Unit: MB/s.
        self.throughput = throughput
        # The type of the cloud disk. Valid values:
        # 
        # - system: system cloud disk.
        # - data: data cloud disk.
        self.type = type
        # The zone ID of the cloud disk.
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_time is not None:
            result['AttachedTime'] = self.attached_time

        if self.bdf_id is not None:
            result['BdfId'] = self.bdf_id

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.delete_auto_snapshot is not None:
            result['DeleteAutoSnapshot'] = self.delete_auto_snapshot

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.description is not None:
            result['Description'] = self.description

        if self.detached_time is not None:
            result['DetachedTime'] = self.detached_time

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.enable_auto_snapshot is not None:
            result['EnableAutoSnapshot'] = self.enable_auto_snapshot

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.iops is not None:
            result['IOPS'] = self.iops

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.mount_instance_num is not None:
            result['MountInstanceNum'] = self.mount_instance_num

        if self.multi_attach is not None:
            result['MultiAttach'] = self.multi_attach

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.portable is not None:
            result['Portable'] = self.portable

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size is not None:
            result['Size'] = self.size

        if self.source_snapshot_id is not None:
            result['SourceSnapshotId'] = self.source_snapshot_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_cluster_id is not None:
            result['StorageClusterId'] = self.storage_cluster_id

        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id

        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.throughput is not None:
            result['Throughput'] = self.throughput

        if self.type is not None:
            result['Type'] = self.type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedTime') is not None:
            self.attached_time = m.get('AttachedTime')

        if m.get('BdfId') is not None:
            self.bdf_id = m.get('BdfId')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('DeleteAutoSnapshot')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DetachedTime') is not None:
            self.detached_time = m.get('DetachedTime')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('EnableAutoSnapshot') is not None:
            self.enable_auto_snapshot = m.get('EnableAutoSnapshot')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('IOPS') is not None:
            self.iops = m.get('IOPS')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('MountInstanceNum') is not None:
            self.mount_instance_num = m.get('MountInstanceNum')

        if m.get('MultiAttach') is not None:
            self.multi_attach = m.get('MultiAttach')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Portable') is not None:
            self.portable = m.get('Portable')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SourceSnapshotId') is not None:
            self.source_snapshot_id = m.get('SourceSnapshotId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClusterId') is not None:
            self.storage_cluster_id = m.get('StorageClusterId')

        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')

        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDiskTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDiskTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

