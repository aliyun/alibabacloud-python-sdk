# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: List[main_models.DescribeSnapshotsResponseBodySnapshots] = None,
        total_count: int = None,
    ):
        # The page number of the current query.
        self.page_number = page_number
        # The number of entries per page in a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The collection of snapshot details.
        self.snapshots = snapshots
        # The total number of snapshots.
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
                temp_model = main_models.DescribeSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        size: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_disk_category: str = None,
        source_disk_id: str = None,
        source_disk_type: str = None,
        source_ens_region_id: str = None,
        source_snapshot_id: str = None,
        status: str = None,
    ):
        # The creation time. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ss format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description.
        self.description = description
        # The ID of the ENS edge zone.
        self.ens_region_id = ens_region_id
        # The disk capacity. Unit: MiB.
        self.size = size
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The display name of the snapshot. This field is returned if a display name was specified when the snapshot was created.
        self.snapshot_name = snapshot_name
        # The snapshot type.
        self.snapshot_type = snapshot_type
        # The disk type. Valid values:
        # 
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: all-flash cloud disk.
        # - local_hdd: local HDD.
        # - local_ssd: local SSD.
        self.source_disk_category = source_disk_category
        # The ID of the source cloud disk. This field is retained even if the source cloud disk of the snapshot has been released.
        self.source_disk_id = source_disk_id
        # The disk property. Valid values:
        # 
        # - 1: system cloud disk.
        # - 2: data cloud disk.
        self.source_disk_type = source_disk_type
        # The ID of the source ENS edge zone.
        self.source_ens_region_id = source_ens_region_id
        # The ID of the source snapshot.
        self.source_snapshot_id = source_snapshot_id
        # The snapshot status. Valid values:
        # 
        # - creating: The snapshot is being created.
        # - available: The snapshot is available.
        # - deleting: The snapshot is being deleted.
        # - error: An error occurred.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.source_disk_category is not None:
            result['SourceDiskCategory'] = self.source_disk_category

        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.source_ens_region_id is not None:
            result['SourceEnsRegionId'] = self.source_ens_region_id

        if self.source_snapshot_id is not None:
            result['SourceSnapshotId'] = self.source_snapshot_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('SourceDiskCategory') is not None:
            self.source_disk_category = m.get('SourceDiskCategory')

        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('SourceEnsRegionId') is not None:
            self.source_ens_region_id = m.get('SourceEnsRegionId')

        if m.get('SourceSnapshotId') is not None:
            self.source_snapshot_id = m.get('SourceSnapshotId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

