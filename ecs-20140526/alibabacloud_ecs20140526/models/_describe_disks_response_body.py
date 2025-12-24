# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDisksResponseBody(DaraModel):
    def __init__(
        self,
        disks: main_models.DescribeDisksResponseBodyDisks = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the disks.
        self.disks = disks
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # >  This parameter will be removed in the future. We recommend that you use `NextToken` and `MaxResults` for a paged query.
        self.page_number = page_number
        # >  This parameter will be removed in the future. We recommend that you use `NextToken` and `MaxResults` for a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        # 
        # > When using the `MaxResults` and `NextToken` parameters for a paginated query, the returned `TotalCount` parameter value is invalid.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disks') is not None:
            temp_model = main_models.DescribeDisksResponseBodyDisks()
            self.disks = temp_model.from_map(m.get('Disks'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDisksResponseBodyDisks(DaraModel):
    def __init__(
        self,
        disk: List[main_models.DescribeDisksResponseBodyDisksDisk] = None,
    ):
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
                temp_model = main_models.DescribeDisksResponseBodyDisksDisk()
                self.disk.append(temp_model.from_map(k1))

        return self

class DescribeDisksResponseBodyDisksDisk(DaraModel):
    def __init__(
        self,
        attached_time: str = None,
        attachments: main_models.DescribeDisksResponseBodyDisksDiskAttachments = None,
        auto_snapshot_policy_id: str = None,
        bdf_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        creation_time: str = None,
        delete_auto_snapshot: bool = None,
        delete_with_instance: bool = None,
        description: str = None,
        detached_time: str = None,
        device: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_name: str = None,
        enable_auto_snapshot: bool = None,
        enable_automated_snapshot_policy: bool = None,
        encrypted: bool = None,
        expired_time: str = None,
        iops: int = None,
        iopsread: int = None,
        iopswrite: int = None,
        image_id: str = None,
        instance_id: str = None,
        kmskey_id: str = None,
        mount_instance_num: int = None,
        mount_instances: main_models.DescribeDisksResponseBodyDisksDiskMountInstances = None,
        multi_attach: str = None,
        operation_locks: main_models.DescribeDisksResponseBodyDisksDiskOperationLocks = None,
        performance_level: str = None,
        placement: main_models.DescribeDisksResponseBodyDisksDiskPlacement = None,
        portable: bool = None,
        product_code: str = None,
        provisioned_iops: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        serial_number: str = None,
        size: int = None,
        source_snapshot_id: str = None,
        status: str = None,
        storage_cluster_id: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        tags: main_models.DescribeDisksResponseBodyDisksDiskTags = None,
        throughput: int = None,
        throughput_read: int = None,
        throughput_write: int = None,
        type: str = None,
        zone_id: str = None,
    ):
        # The time when the disk was last attached. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mmZ format. The time is displayed in UTC.
        self.attached_time = attached_time
        # The attachment information of the disk. The value is an array that consists of the `Attachment` values. This value is not returned when you query Shared Block Storage devices.
        self.attachments = attachments
        # The ID of the automatic snapshot policy that is applied to the cloud disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # This parameter is in invitational preview and is not publicly available.
        self.bdf_id = bdf_id
        # Indicates whether the performance burst feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is available only if you set `Category` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The category of the disk. Valid values:
        # 
        # *   cloud: basic disk
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: ESSD
        # *   cloud_auto: ESSD AutoPL disk
        # *   local_ssd_pro: I/O-intensive local disk
        # *   local_hdd_pro: throughput-intensive local disk
        # *   cloud_essd_entry: ESSD Entry disk
        # *   elastic_ephemeral_disk_standard: standard elastic ephemeral disk
        # *   elastic_ephemeral_disk_premium: premium static ephemeral disk
        # *   ephemeral: retired local disk
        # *   ephemeral_ssd: retired local SSD
        self.category = category
        # The time when the disk was created.
        self.creation_time = creation_time
        # Indicates whether the automatic snapshots of the cloud disk are deleted when the cloud disk is released. Valid values:
        # 
        # *   true: The automatic snapshots of the cloud disk are deleted when the disk is released.
        # *   false: The automatic snapshots of the cloud disk are retained when the disk is released.
        # 
        # Snapshots that were created in the ECS console or by calling the [CreateSnapshot](https://help.aliyun.com/document_detail/25524.html) operation are retained and not affected by this parameter.
        self.delete_auto_snapshot = delete_auto_snapshot
        # Indicates whether the disk is released when the instance to which the disk is attached is released. Valid values:
        # 
        # *   true: The disk is released when the associated instance is released.
        # *   false: The disk is retained when the associated instance is released.
        self.delete_with_instance = delete_with_instance
        # The description of the disk.
        self.description = description
        # The time when the disk was last detached.
        self.detached_time = detached_time
        # The device name of the disk on the instance to which the disk is attached. Example: /dev/xvdb. Take note of the following items:
        # 
        # *   This parameter has a value only when the `Status` value is `In_use` or `Detaching`.
        # *   This parameter is empty for cloud disks for which the multi-attach feature is enabled. You can query the attachment information of the cloud disk based on the returned list of `Attachment` objects.
        # 
        # >  This parameter will be removed in the future. We recommend that you use other parameters to ensure future compatibility.
        self.device = device
        # The billing method of the disk. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        self.disk_charge_type = disk_charge_type
        # The ID of the disk.
        self.disk_id = disk_id
        # The name of the disk.
        self.disk_name = disk_name
        # Indicates whether the automatic snapshot policy feature is enabled for the cloud disk.
        # 
        # >  This parameter is deprecated. By default, the automatic snapshot policy feature is enabled for cloud disks. You need to only apply an automatic snapshot policy to a cloud disk before you can use the automatic snapshot policy.
        self.enable_auto_snapshot = enable_auto_snapshot
        # Indicates whether an automatic snapshot policy is applied to the cloud disk.
        self.enable_automated_snapshot_policy = enable_automated_snapshot_policy
        # Indicates whether the cloud disk is encrypted.
        self.encrypted = encrypted
        # The time when the subscription disk expires.
        self.expired_time = expired_time
        # The maximum number of read and write operations per second.
        self.iops = iops
        # The maximum number of read operations per second.
        self.iopsread = iopsread
        # The maximum number of write operations per second.
        self.iopswrite = iopswrite
        # The ID of the image that was used to create the instance. This parameter is empty unless the cloud disk was created from an image. The value of this parameter remains unchanged throughout the lifecycle of the cloud disk.
        self.image_id = image_id
        # The ID of the instance to which the disk is attached. Take note of the following items:
        # 
        # *   This parameter has a value only when the `Status` value is `In_use` or `Detaching`.
        # *   This parameter is empty for cloud disks for which the multi-attach feature is enabled. You can query the attachment information of the cloud disk based on the returned `Attachment` objects.
        self.instance_id = instance_id
        # The ID of the KMS key that is used for the cloud disk.
        self.kmskey_id = kmskey_id
        # The number of instances to which the Shared Block Storage device is attached.
        self.mount_instance_num = mount_instance_num
        # The attachment information of the Shared Block Storage device.
        self.mount_instances = mount_instances
        # Indicates whether the multi-attach feature is enabled for the cloud disk.
        self.multi_attach = multi_attach
        # The reasons why the disk was locked.
        self.operation_locks = operation_locks
        # The performance level of the ESSD. Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level
        # The locations in which data is stored.
        # 
        # This parameter is returned only if you specify `Placement` in the AdditionalAttributes.N request parameter.
        # 
        # >  This parameter is valid only for Regional ESSDs (cloud_regional_disk_auto).
        self.placement = placement
        # Indicates whether the disk is removable.
        self.portable = portable
        # The product code of the disk in Alibaba Cloud Marketplace.
        self.product_code = product_code
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1,000 × *Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × *Capacity, 50,000}
        # 
        # This parameter is available only if you set `Category` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The ID of the region to which the disk belongs.
        self.region_id = region_id
        # The ID of the resource group to which the disk belongs.
        self.resource_group_id = resource_group_id
        # The serial number of the disk.
        self.serial_number = serial_number
        # The size of the disk. Unit: GiB.
        self.size = size
        # The ID of the snapshot that was used to create the cloud disk.
        # 
        # This parameter is empty unless the cloud disk was created from a snapshot. The value of this parameter remains unchanged throughout the lifecycle of the cloud disk.
        self.source_snapshot_id = source_snapshot_id
        # The status of the disk. Valid values:
        # 
        # *   In_use
        # *   Available
        # *   Attaching
        # *   Detaching
        # *   Creating
        # *   ReIniting
        self.status = status
        # The ID of the dedicated block storage cluster to which the cloud disk belongs. If your cloud disk belongs to the public block storage cluster, an empty value is returned.
        self.storage_cluster_id = storage_cluster_id
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set.
        self.storage_set_partition_number = storage_set_partition_number
        # The tags of the disk.
        self.tags = tags
        # The amount of data that can be transferred per second. Unit: MB/s.
        self.throughput = throughput
        # The amount of data that can be read per second. Unit: MB/s.
        self.throughput_read = throughput_read
        # The amount of data that can be written per second. Unit: MB/s.
        self.throughput_write = throughput_write
        # The type of the disk. Valid values:
        # 
        # *   system: system disk
        # *   data: data disk
        self.type = type
        # The ID of the zone to which the disk belongs.
        self.zone_id = zone_id

    def validate(self):
        if self.attachments:
            self.attachments.validate()
        if self.mount_instances:
            self.mount_instances.validate()
        if self.operation_locks:
            self.operation_locks.validate()
        if self.placement:
            self.placement.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_time is not None:
            result['AttachedTime'] = self.attached_time

        if self.attachments is not None:
            result['Attachments'] = self.attachments.to_map()

        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.bdf_id is not None:
            result['BdfId'] = self.bdf_id

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

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

        if self.enable_automated_snapshot_policy is not None:
            result['EnableAutomatedSnapshotPolicy'] = self.enable_automated_snapshot_policy

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.iops is not None:
            result['IOPS'] = self.iops

        if self.iopsread is not None:
            result['IOPSRead'] = self.iopsread

        if self.iopswrite is not None:
            result['IOPSWrite'] = self.iopswrite

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.mount_instance_num is not None:
            result['MountInstanceNum'] = self.mount_instance_num

        if self.mount_instances is not None:
            result['MountInstances'] = self.mount_instances.to_map()

        if self.multi_attach is not None:
            result['MultiAttach'] = self.multi_attach

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.placement is not None:
            result['Placement'] = self.placement.to_map()

        if self.portable is not None:
            result['Portable'] = self.portable

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

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

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.throughput is not None:
            result['Throughput'] = self.throughput

        if self.throughput_read is not None:
            result['ThroughputRead'] = self.throughput_read

        if self.throughput_write is not None:
            result['ThroughputWrite'] = self.throughput_write

        if self.type is not None:
            result['Type'] = self.type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedTime') is not None:
            self.attached_time = m.get('AttachedTime')

        if m.get('Attachments') is not None:
            temp_model = main_models.DescribeDisksResponseBodyDisksDiskAttachments()
            self.attachments = temp_model.from_map(m.get('Attachments'))

        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('BdfId') is not None:
            self.bdf_id = m.get('BdfId')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

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

        if m.get('EnableAutomatedSnapshotPolicy') is not None:
            self.enable_automated_snapshot_policy = m.get('EnableAutomatedSnapshotPolicy')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('IOPS') is not None:
            self.iops = m.get('IOPS')

        if m.get('IOPSRead') is not None:
            self.iopsread = m.get('IOPSRead')

        if m.get('IOPSWrite') is not None:
            self.iopswrite = m.get('IOPSWrite')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('MountInstanceNum') is not None:
            self.mount_instance_num = m.get('MountInstanceNum')

        if m.get('MountInstances') is not None:
            temp_model = main_models.DescribeDisksResponseBodyDisksDiskMountInstances()
            self.mount_instances = temp_model.from_map(m.get('MountInstances'))

        if m.get('MultiAttach') is not None:
            self.multi_attach = m.get('MultiAttach')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeDisksResponseBodyDisksDiskOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Placement') is not None:
            temp_model = main_models.DescribeDisksResponseBodyDisksDiskPlacement()
            self.placement = temp_model.from_map(m.get('Placement'))

        if m.get('Portable') is not None:
            self.portable = m.get('Portable')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

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

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeDisksResponseBodyDisksDiskTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')

        if m.get('ThroughputRead') is not None:
            self.throughput_read = m.get('ThroughputRead')

        if m.get('ThroughputWrite') is not None:
            self.throughput_write = m.get('ThroughputWrite')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDisksResponseBodyDisksDiskTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeDisksResponseBodyDisksDiskTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDisksResponseBodyDisksDiskTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDisksResponseBodyDisksDiskTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the disk.
        self.tag_key = tag_key
        # The tag value of the disk.
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

class DescribeDisksResponseBodyDisksDiskPlacement(DaraModel):
    def __init__(
        self,
        zone_ids: str = None,
    ):
        # The IDs of the zones in which data is stored.
        self.zone_ids = zone_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

class DescribeDisksResponseBodyDisksDiskOperationLocks(DaraModel):
    def __init__(
        self,
        operation_lock: List[main_models.DescribeDisksResponseBodyDisksDiskOperationLocksOperationLock] = None,
    ):
        self.operation_lock = operation_lock

    def validate(self):
        if self.operation_lock:
            for v1 in self.operation_lock:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperationLock'] = []
        if self.operation_lock is not None:
            for k1 in self.operation_lock:
                result['OperationLock'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_lock = []
        if m.get('OperationLock') is not None:
            for k1 in m.get('OperationLock'):
                temp_model = main_models.DescribeDisksResponseBodyDisksDiskOperationLocksOperationLock()
                self.operation_lock.append(temp_model.from_map(k1))

        return self

class DescribeDisksResponseBodyDisksDiskOperationLocksOperationLock(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the disk was locked.
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

class DescribeDisksResponseBodyDisksDiskMountInstances(DaraModel):
    def __init__(
        self,
        mount_instance: List[main_models.DescribeDisksResponseBodyDisksDiskMountInstancesMountInstance] = None,
    ):
        self.mount_instance = mount_instance

    def validate(self):
        if self.mount_instance:
            for v1 in self.mount_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MountInstance'] = []
        if self.mount_instance is not None:
            for k1 in self.mount_instance:
                result['MountInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_instance = []
        if m.get('MountInstance') is not None:
            for k1 in m.get('MountInstance'):
                temp_model = main_models.DescribeDisksResponseBodyDisksDiskMountInstancesMountInstance()
                self.mount_instance.append(temp_model.from_map(k1))

        return self

class DescribeDisksResponseBodyDisksDiskMountInstancesMountInstance(DaraModel):
    def __init__(
        self,
        attached_time: str = None,
        device: str = None,
        instance_id: str = None,
    ):
        # The time when the disk was attached. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.attached_time = attached_time
        # The mount point of the disk.
        self.device = device
        # The ID of the instance to which the disk is attached.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_time is not None:
            result['AttachedTime'] = self.attached_time

        if self.device is not None:
            result['Device'] = self.device

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedTime') is not None:
            self.attached_time = m.get('AttachedTime')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class DescribeDisksResponseBodyDisksDiskAttachments(DaraModel):
    def __init__(
        self,
        attachment: List[main_models.DescribeDisksResponseBodyDisksDiskAttachmentsAttachment] = None,
    ):
        self.attachment = attachment

    def validate(self):
        if self.attachment:
            for v1 in self.attachment:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attachment'] = []
        if self.attachment is not None:
            for k1 in self.attachment:
                result['Attachment'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachment = []
        if m.get('Attachment') is not None:
            for k1 in m.get('Attachment'):
                temp_model = main_models.DescribeDisksResponseBodyDisksDiskAttachmentsAttachment()
                self.attachment.append(temp_model.from_map(k1))

        return self

class DescribeDisksResponseBodyDisksDiskAttachmentsAttachment(DaraModel):
    def __init__(
        self,
        attached_time: str = None,
        device: str = None,
        instance_id: str = None,
    ):
        # The time when the disk was attached. The time is displayed in UTC.
        self.attached_time = attached_time
        # The device name of the disk.
        self.device = device
        # The ID of the instance to which the disk is attached.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_time is not None:
            result['AttachedTime'] = self.attached_time

        if self.device is not None:
            result['Device'] = self.device

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedTime') is not None:
            self.attached_time = m.get('AttachedTime')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

