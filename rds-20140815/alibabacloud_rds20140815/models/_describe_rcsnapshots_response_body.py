# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: List[main_models.DescribeRCSnapshotsResponseBodySnapshots] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The details of snapshots.
        self.snapshots = snapshots
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            for v1 in self.snapshots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['Snapshots'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k1 in m.get('Snapshots'):
                temp_model = main_models.DescribeRCSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRCSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        available: bool = None,
        category: str = None,
        creation_time: str = None,
        description: str = None,
        encrypted: bool = None,
        instant_access: bool = None,
        progress: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_disk_id: str = None,
        source_disk_size: int = None,
        source_disk_type: str = None,
        source_storage_type: str = None,
        status: str = None,
        tag: List[main_models.DescribeRCSnapshotsResponseBodySnapshotsTag] = None,
        usage: str = None,
    ):
        # Indicates whether the snapshot can be shared and used to create or roll back a cloud disk. Valid values:
        # 
        # *   true
        # *   false
        self.available = available
        # The snapshot type. Valid values:
        # 
        # *   Standard: standard snapshot
        # *   Flash: local snapshot This value will be deprecated. The local snapshot feature is replaced with the instant access feature.
        # *   archive: archived snapshot
        self.category = category
        # The creation time. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The snapshot description.
        self.description = description
        # Indicates whether the snapshot was encrypted. Valid values:
        # 
        # *   true
        # *   false
        self.encrypted = encrypted
        # This parameter is deprecated.
        self.instant_access = instant_access
        # The progress of the snapshot creation task in percentage.
        self.progress = progress
        # The region ID.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The snapshot name.
        self.snapshot_name = snapshot_name
        # The snapshot type. Valid values:
        # 
        # *   auto or timer: automatically created snapshot
        # *   user: manually created snapshot
        # *   all: all snapshot types
        self.snapshot_type = snapshot_type
        # The ID of the original disk. This parameter is retained even after the original disk for which the snapshot was created is released.
        self.source_disk_id = source_disk_id
        # The storage capacity of the original disk. Unit: GiB.
        self.source_disk_size = source_disk_size
        # The type of the original disk. Valid values:
        # 
        # *   SYSTEM: system disk
        # *   DATA: data disk
        self.source_disk_type = source_disk_type
        # The type of the source disk.
        # 
        # >  This parameter will be removed in the future. To ensure future compatibility, we recommend that you use other parameters.
        self.source_storage_type = source_storage_type
        # The snapshot status. Valid values:
        # 
        # *   progressing: The snapshot is being created.
        # *   accomplished: The snapshot is created.
        # *   failed: The snapshot fails to be created.
        self.status = status
        self.tag = tag
        # Indicates whether the snapshot is used to create custom images or disks. Valid values:
        # 
        # *   image: The snapshot is used to create custom images.
        # *   disk: The snapshot is used to create disks.
        # *   image_disk: The snapshot is used to create custom images and data disks.
        # *   none: The snapshot is not used to create custom images or disks.
        self.usage = usage

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
        if self.available is not None:
            result['Available'] = self.available

        if self.category is not None:
            result['Category'] = self.category

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.instant_access is not None:
            result['InstantAccess'] = self.instant_access

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id

        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.source_storage_type is not None:
            result['SourceStorageType'] = self.source_storage_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('InstantAccess') is not None:
            self.instant_access = m.get('InstantAccess')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')

        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('SourceStorageType') is not None:
            self.source_storage_type = m.get('SourceStorageType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeRCSnapshotsResponseBodySnapshotsTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class DescribeRCSnapshotsResponseBodySnapshotsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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

