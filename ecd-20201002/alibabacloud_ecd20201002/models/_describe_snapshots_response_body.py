# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        snapshots: List[main_models.DescribeSnapshotsResponseBodySnapshots] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The snapshots.
        self.snapshots = snapshots

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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['Snapshots'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k1 in m.get('Snapshots'):
                temp_model = main_models.DescribeSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        desktop_id: str = None,
        progress: str = None,
        remain_time: int = None,
        restore_point_id: str = None,
        restore_point_name: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_disk_size: str = None,
        source_disk_type: str = None,
        status: str = None,
    ):
        # The time when the snapshot was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The snapshot description.
        self.description = description
        # The ID of the cloud computer to which the snapshot belongs.
        self.desktop_id = desktop_id
        # The progress of creating the cloud computer.
        self.progress = progress
        # The remaining time required to complete snapshot creation. Unit: seconds.
        self.remain_time = remain_time
        # The ID of the restore point.
        self.restore_point_id = restore_point_id
        # The name of the restore point.
        self.restore_point_name = restore_point_name
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The snapshot name.
        self.snapshot_name = snapshot_name
        # The snapshot type.
        # 
        # Valid values:
        # 
        # *   AUTO: an automatic snapshot.
        # *   USER: a manual snapshot.
        self.snapshot_type = snapshot_type
        # The size of the source disk. Unit: GiB.
        self.source_disk_size = source_disk_size
        # The type of the source disk.
        # 
        # Valid values:
        # 
        # *   SYSTEM: a system disk.
        # *   DATA: a data disk.
        self.source_disk_type = source_disk_type
        # The snapshot status.
        # 
        # Valid values:
        # 
        # *   PROGRESSING: The snapshot is being created.
        # *   FAILED: The snapshot failed to be created.
        # *   ACCOMPLISHED: The snapshot is created.
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

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time

        if self.restore_point_id is not None:
            result['RestorePointId'] = self.restore_point_id

        if self.restore_point_name is not None:
            result['RestorePointName'] = self.restore_point_name

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')

        if m.get('RestorePointId') is not None:
            self.restore_point_id = m.get('RestorePointId')

        if m.get('RestorePointName') is not None:
            self.restore_point_name = m.get('RestorePointName')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

