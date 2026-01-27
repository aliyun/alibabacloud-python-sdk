# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCDisksResponseBody(DaraModel):
    def __init__(
        self,
        disks: List[main_models.DescribeRCDisksResponseBodyDisks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the disks.
        self.disks = disks
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

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
        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeRCDisksResponseBodyDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRCDisksResponseBodyDisks(DaraModel):
    def __init__(
        self,
        attached_time: str = None,
        category: str = None,
        creation_time: str = None,
        delete_auto_snapshot: bool = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_name: str = None,
        encrypted: bool = None,
        expired_time: str = None,
        iops: int = None,
        image_id: str = None,
        instance_id: str = None,
        performance_level: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        serial_number: str = None,
        size: int = None,
        source_snapshot_id: str = None,
        status: str = None,
        storage_cluster_id: str = None,
        storage_set_id: str = None,
        tag: List[main_models.DescribeRCDisksResponseBodyDisksTag] = None,
        type: str = None,
        zone_id: str = None,
    ):
        self.attached_time = attached_time
        # The category of the disk. Valid values:
        # 
        # *   **cloud_efficiency**: ultra disk.
        # *   **cloud_ssd**: standard SSD.
        # *   **cloud_essd**: ESSD.
        # *   **cloud_auto**: Premium ESSD
        self.category = category
        # The creation time.
        self.creation_time = creation_time
        # Indicates whether the automatic snapshots of the cloud disk are deleted after the disk is released. Valid values:
        # 
        # *   true
        # *   false
        self.delete_auto_snapshot = delete_auto_snapshot
        # Indicates whether the cloud disk is released when its associated instance is released. Valid values:
        # 
        # *   true
        # *   false
        self.delete_with_instance = delete_with_instance
        # The disk description.
        self.description = description
        # The mount point of the disk.
        self.device = device
        # The billing method of the disk.
        # 
        # Only **PostPaid** (pay-as-you-go) is supported.
        self.disk_charge_type = disk_charge_type
        # The disk ID.
        self.disk_id = disk_id
        # The disk name.
        self.disk_name = disk_name
        # Indicates whether only encrypted cloud disks are queried. Valid values:
        # 
        # *   true
        # *   false (default)
        self.encrypted = encrypted
        # A reserved parameter. You do not need to specify this parameter.
        self.expired_time = expired_time
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1,000 × *Capacity - Baseline performance}. Baseline performance = min{1,800 + 50 × *Capacity, 50,000}
        # 
        # This parameter is available only when the `Category` parameter is set to `cloud_auto`.
        self.iops = iops
        # The ID of the image that is used to create the instance. This parameter is returned only if the cloud disk is created from an image. The value of this parameter remains unchanged throughout the lifecycle of the cloud disk.
        self.image_id = image_id
        # The instance ID.
        self.instance_id = instance_id
        # The performance level (PL) of the ESSD. Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level
        # The region ID.
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
        # *   In_use: The disk is in use.
        # *   Available: The disk can be attached.
        # *   Attaching: The disk is being attached.
        # *   Detaching: The cloud disk is being detached.
        # *   Creating: The disk is being created.
        # *   ReIniting: The disk is being initialized.
        self.status = status
        # The ID of the dedicated block storage cluster to which the cloud disk belongs. If your cloud disk belongs to the public block storage cluster, an empty value is returned.
        self.storage_cluster_id = storage_cluster_id
        # The storage set ID.
        self.storage_set_id = storage_set_id
        # The list of tags.
        self.tag = tag
        # The disk type. Valid values:
        # 
        # *   system: system disk
        # *   data: data disk
        self.type = type
        # The zone ID.
        self.zone_id = zone_id

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
        if self.attached_time is not None:
            result['AttachedTime'] = self.attached_time

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

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.iops is not None:
            result['IOPS'] = self.iops

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedTime') is not None:
            self.attached_time = m.get('AttachedTime')

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

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('IOPS') is not None:
            self.iops = m.get('IOPS')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeRCDisksResponseBodyDisksTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeRCDisksResponseBodyDisksTag(DaraModel):
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

