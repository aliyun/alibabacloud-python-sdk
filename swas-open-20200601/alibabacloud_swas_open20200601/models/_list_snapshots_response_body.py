# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: List[main_models.ListSnapshotsResponseBodySnapshots] = None,
        total_count: int = None,
    ):
        # The page number of the snapshot list.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The snapshot information.
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
                temp_model = main_models.ListSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        instance_id: str = None,
        progress: str = None,
        region_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
        rollback_time: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        source_disk_id: str = None,
        source_disk_type: str = None,
        status: str = None,
        tags: List[main_models.ListSnapshotsResponseBodySnapshotsTags] = None,
    ):
        # The time when the snapshot was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The instance ID of the simple application server.
        # 
        # Note: This field has a value for system cloud disk snapshots and is empty for data cloud disk snapshots.
        self.instance_id = instance_id
        # The progress of snapshot creation.
        self.progress = progress
        # The region ID.
        self.region_id = region_id
        # The remarks of the snapshot.
        self.remark = remark
        # The ID of the resource group to which the snapshot belongs.
        self.resource_group_id = resource_group_id
        # The time of the most recent rollback. The time is in the UTC (Z) time zone in the YYYY-MM-DDThh:mm:ssZ format.
        self.rollback_time = rollback_time
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The snapshot name.
        self.snapshot_name = snapshot_name
        # The ID of the source disk. This value is retained even if the source disk of the snapshot has been released.
        self.source_disk_id = source_disk_id
        # The type of the source disk for the snapshot. Valid values:
        # - System: system cloud disk.
        # - Data: data cloud disk.
        self.source_disk_type = source_disk_type
        # The snapshot status. Valid values:
        # 
        # - progressing: The snapshot is being created.
        # - accomplished: The snapshot is created.
        # - failed: The snapshot failed to be created.
        # - disabled: Rollback is not supported.
        self.status = status
        # The tags of the snapshot.
        self.tags = tags

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
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rollback_time is not None:
            result['RollbackTime'] = self.rollback_time

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RollbackTime') is not None:
            self.rollback_time = m.get('RollbackTime')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListSnapshotsResponseBodySnapshotsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListSnapshotsResponseBodySnapshotsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the snapshot.
        self.key = key
        # The tag value of the snapshot.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

