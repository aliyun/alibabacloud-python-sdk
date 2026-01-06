# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: main_models.DescribeSnapshotsResponseBodySnapshots = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The details about snapshots.
        self.snapshots = snapshots
        # The total number of snapshots returned.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

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

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()

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
        completed_time: str = None,
        create_time: str = None,
        description: str = None,
        encrypt_type: int = None,
        file_system_type: str = None,
        progress: str = None,
        remain_time: int = None,
        retention_days: int = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_file_system_id: str = None,
        source_file_system_size: int = None,
        source_file_system_version: str = None,
        status: str = None,
    ):
        # The time when snapshot creation was complete.
        # 
        # The time follows the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard in UTC. The time is displayed in the `yyyy-MM-ddThh:mmZ` format.
        # 
        # >  This parameter is valid only when the snapshot is created. During snapshot creation, the value of this parameter is the same as that of CreateTime.
        self.completed_time = completed_time
        # The time when the snapshot was created.
        # 
        # The time follows the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) standard in UTC. The time is displayed in the `yyyy-MM-ddThh:mmZ` format.
        self.create_time = create_time
        # The description of the snapshot.
        self.description = description
        # Indicates whether the snapshot is encrypted.
        # 
        # Valid values:
        # 
        # *   0: The snapshot is not encrypted.
        # *   1: The snapshot is encrypted.
        self.encrypt_type = encrypt_type
        # The type of the file system.
        self.file_system_type = file_system_type
        # The progress of the snapshot creation. The value of this parameter is expressed as a percentage.
        self.progress = progress
        # The remaining time that is required to create the snapshot.
        # 
        # Unit: seconds.
        self.remain_time = remain_time
        # The retention period of the auto snapshot.
        # 
        # Unit: days.
        # 
        # Valid values:
        # 
        # *   \\-1: Auto snapshots are permanently retained. After the number of auto snapshots exceeds the upper limit, the earliest auto snapshot is automatically deleted.
        # *   1 to 65536: Auto snapshots are retained for the specified days. After the retention period of auto snapshots expires, the auto snapshots are automatically deleted.
        self.retention_days = retention_days
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The snapshot name.
        # 
        # If you specify a name to create a snapshot, the name of the snapshot is returned. Otherwise, no value is returned for this parameter.
        self.snapshot_name = snapshot_name
        # The snapshot type. Valid values:
        # 
        # *   auto: automatically created snapshots
        # *   user: manually created snapshots
        self.snapshot_type = snapshot_type
        # The ID of the source file system.
        # 
        # This parameter is retained even if the source file system of the snapshot is deleted.
        self.source_file_system_id = source_file_system_id
        # The capacity of the source file system.
        # 
        # Unit: GiB.
        self.source_file_system_size = source_file_system_size
        # The version of the source file system.
        self.source_file_system_version = source_file_system_version
        # The status of the snapshot.
        # 
        # Valid values:
        # 
        # *   progressing: The snapshot is being created.
        # *   accomplished: The snapshot is created.
        # *   failed: The snapshot fails to be created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_time is not None:
            result['CompletedTime'] = self.completed_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type

        if self.source_file_system_id is not None:
            result['SourceFileSystemId'] = self.source_file_system_id

        if self.source_file_system_size is not None:
            result['SourceFileSystemSize'] = self.source_file_system_size

        if self.source_file_system_version is not None:
            result['SourceFileSystemVersion'] = self.source_file_system_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedTime') is not None:
            self.completed_time = m.get('CompletedTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')

        if m.get('SourceFileSystemId') is not None:
            self.source_file_system_id = m.get('SourceFileSystemId')

        if m.get('SourceFileSystemSize') is not None:
            self.source_file_system_size = m.get('SourceFileSystemSize')

        if m.get('SourceFileSystemVersion') is not None:
            self.source_file_system_version = m.get('SourceFileSystemVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

