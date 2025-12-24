# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: main_models.DescribeSnapshotsResponseBodySnapshots = None,
        total_count: int = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # >  This parameter will be removed in the future. We recommend that you use NextToken and MaxResults for a paged query.
        self.page_number = page_number
        # >  This parameter will be removed in the future. We recommend that you use NextToken and MaxResults for a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Details about the snapshots.
        self.snapshots = snapshots
        # The total number of snapshots.
        # 
        # > When using the `MaxResults` and `NextToken` parameters for a paginated query, the returned `TotalCount` parameter value is invalid.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Snapshots') is not None:
            temp_model = main_models.DescribeSnapshotsResponseBodySnapshots()
            self.snapshots = temp_model.from_map(m.get('Snapshots'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        snapshot: List[main_models.DescribeSnapshotsResponseBodySnapshotsSnapshot] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            for v1 in self.snapshot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k1 in self.snapshot:
                result['Snapshot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k1 in m.get('Snapshot'):
                temp_model = main_models.DescribeSnapshotsResponseBodySnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotsResponseBodySnapshotsSnapshot(DaraModel):
    def __init__(
        self,
        available: bool = None,
        category: str = None,
        creation_time: str = None,
        description: str = None,
        encrypted: bool = None,
        instant_access: bool = None,
        instant_access_retention_days: int = None,
        kmskey_id: str = None,
        last_modified_time: str = None,
        product_code: str = None,
        progress: str = None,
        region_id: str = None,
        remain_time: int = None,
        resource_group_id: str = None,
        retention_days: int = None,
        snapshot_id: str = None,
        snapshot_link_id: str = None,
        snapshot_name: str = None,
        snapshot_sn: str = None,
        snapshot_type: str = None,
        source_disk_id: str = None,
        source_disk_size: str = None,
        source_disk_type: str = None,
        source_region_id: str = None,
        source_snapshot_id: str = None,
        source_storage_type: str = None,
        status: str = None,
        tags: main_models.DescribeSnapshotsResponseBodySnapshotsSnapshotTags = None,
        usage: str = None,
    ):
        # Indicates whether the snapshot can be shared and be used to create or roll back a cloud disk. Valid values:
        # 
        # *   true
        # *   false
        self.available = available
        # The category of the snapshot. Valid values:
        # 
        # *   Standard: standard snapshot.
        # *   Flash: local snapshot. This value will be deprecated. The local snapshot feature is replaced by the instant access feature.
        # *   archive: archive snapshot.
        self.category = category
        # The time when the snapshot was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the snapshot.
        self.description = description
        # Indicates whether the snapshot was encrypted. Valid values:
        # 
        # *   true
        # *   false
        self.encrypted = encrypted
        # Indicates whether the instant access feature is enabled. Valid values:
        # 
        # *   true: The instant access feature is enabled. By default, the instant access feature is enabled for Enterprise SSDs (ESSDs) and ESSD Entry disks.
        # *   false: The instant access feature is disabled. The snapshot is a standard snapshot for which the instant access feature is disabled.
        # 
        # >  This parameter is deprecated. By default, new standard snapshots of ESSDs are upgraded to instant access snapshots free of charge without the need for additional configurations. For more information, see [Use the instant access feature](https://help.aliyun.com/document_detail/193667.html).
        self.instant_access = instant_access
        # Indicates the validity period of the instant access feature. When the validity period ends, the instant access feature is automatically disabled.
        # 
        # By default, the value of this parameter is the same as the value of `RetentionDays`.
        # 
        # >  This parameter is deprecated. By default, new standard snapshots of ESSDs are upgraded to instant access snapshots free of charge without the need for additional configurations. For more information, see [Use the instant access feature](https://help.aliyun.com/document_detail/193667.html).
        self.instant_access_retention_days = instant_access_retention_days
        # The ID of the KMS key used for the data disk.
        self.kmskey_id = kmskey_id
        # The time when the snapshot was last modified. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.last_modified_time = last_modified_time
        # The product code of the Alibaba Cloud Marketplace image.
        self.product_code = product_code
        # The progress of the snapshot creation task. Unit: percent (%).
        self.progress = progress
        # The region ID of the snapshot.
        self.region_id = region_id
        # The amount of remaining time required to create the snapshot. Unit: seconds.
        self.remain_time = remain_time
        # The ID of the resource group to which the snapshot belongs.
        self.resource_group_id = resource_group_id
        # The retention period of the automatic snapshot. Unit: days.
        self.retention_days = retention_days
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id
        # The ID of the snapshot chain that is associated with the snapshot.
        self.snapshot_link_id = snapshot_link_id
        # The name of the snapshot. This parameter is returned only if a snapshot name was specified when the snapshot was created.
        self.snapshot_name = snapshot_name
        # The serial number of the snapshot.
        self.snapshot_sn = snapshot_sn
        # The type of the snapshot. Valid values:
        # 
        # *   auto or timer: automatic snapshot
        # *   user: manual snapshot
        # *   all: all snapshot types
        self.snapshot_type = snapshot_type
        # The ID of the source disk. This parameter is retained even after the source disk is released.
        self.source_disk_id = source_disk_id
        # The capacity of the source disk. Unit: GiB.
        self.source_disk_size = source_disk_size
        # The type of the source disk. Valid values:
        # 
        # *   system
        # *   data
        self.source_disk_type = source_disk_type
        # The region ID of the source snapshot.
        self.source_region_id = source_region_id
        # The ID of the source snapshot.
        self.source_snapshot_id = source_snapshot_id
        # The category of the source disk.
        # 
        # >  This parameter will be removed in the future. We recommend that you use other parameters to ensure future compatibility.
        self.source_storage_type = source_storage_type
        # The status of the snapshot. Valid values:
        # 
        # *   progressing: The snapshot is being created.
        # *   accomplished: The snapshot is created.
        # *   failed: The snapshot failed to be created.
        self.status = status
        # The tags of the snapshot.
        self.tags = tags
        # Indicates whether the snapshot was used to create images or cloud disks. Valid values:
        # 
        # *   image: The snapshot was used to create custom images.
        # *   disk: The snapshot was used to create cloud disks.
        # *   image_disk: The snapshot was used to create custom images and data disks.
        # *   none: The snapshot was not used to create custom images or cloud disks.
        self.usage = usage

    def validate(self):
        if self.tags:
            self.tags.validate()

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

        if self.instant_access_retention_days is not None:
            result['InstantAccessRetentionDays'] = self.instant_access_retention_days

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_link_id is not None:
            result['SnapshotLinkId'] = self.snapshot_link_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_sn is not None:
            result['SnapshotSN'] = self.snapshot_sn

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id

        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        if self.source_snapshot_id is not None:
            result['SourceSnapshotId'] = self.source_snapshot_id

        if self.source_storage_type is not None:
            result['SourceStorageType'] = self.source_storage_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

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

        if m.get('InstantAccessRetentionDays') is not None:
            self.instant_access_retention_days = m.get('InstantAccessRetentionDays')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotLinkId') is not None:
            self.snapshot_link_id = m.get('SnapshotLinkId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotSN') is not None:
            self.snapshot_sn = m.get('SnapshotSN')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')

        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        if m.get('SourceSnapshotId') is not None:
            self.source_snapshot_id = m.get('SourceSnapshotId')

        if m.get('SourceStorageType') is not None:
            self.source_storage_type = m.get('SourceStorageType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeSnapshotsResponseBodySnapshotsSnapshotTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class DescribeSnapshotsResponseBodySnapshotsSnapshotTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeSnapshotsResponseBodySnapshotsSnapshotTagsTag] = None,
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
                temp_model = main_models.DescribeSnapshotsResponseBodySnapshotsSnapshotTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotsResponseBodySnapshotsSnapshotTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the snapshot.
        self.tag_key = tag_key
        # The tag value of the snapshot.
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

