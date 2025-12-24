# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        snapshots: List[main_models.DescribeSnapshotsResponseBodySnapshots] = None,
    ):
        # If the NextToken parameter is empty, no next page exists.
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
        creator: str = None,
        deletion_time: str = None,
        description: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        disk_status: str = None,
        os_type: str = None,
        progress: str = None,
        protocol_type: str = None,
        remain_time: int = None,
        restore_point_id: str = None,
        restore_point_name: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_disk_size: str = None,
        source_disk_type: str = None,
        status: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        # The point in time at which the snapshot was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-mm-ddthh:mm:ssz` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The user who creates the snapshot.
        self.creator = creator
        # The time when the snapshot was deleted. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-mm-ddthh:mm:ssz` format. The time is displayed in UTC.
        self.deletion_time = deletion_time
        # The description of the snapshot.
        self.description = description
        # The ID of the cloud computer to which the snapshot belongs.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # The status of the cloud computer.
        # 
        # Valid values:
        # 
        # *   Stopped
        # *   Starting
        # *   Rebuilding
        # *   Running
        # *   Stopping
        # *   Expired
        # *   Deleted
        # *   Pending
        self.desktop_status = desktop_status
        self.disk_status = disk_status
        self.os_type = os_type
        # The progress of creating the snapshot. Unit: %.
        self.progress = progress
        # The protocol type.
        # 
        # Valid values:
        # 
        # *   HDX: High-definition Experience (HDX) protocol
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ASP: in-house Adaptive Streaming Protocol (ASP)
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.protocol_type = protocol_type
        # The remaining time that is required to complete the snapshot creation. Unit: seconds.
        # 
        # >  When the `Status` value is `PROGRESSING`, the `RemainTime` value is `-1`. A value of -1 indicates that the system is calculating the remaining time.
        self.remain_time = remain_time
        # The ID of the restore point.
        self.restore_point_id = restore_point_id
        # The name of the restore point.
        self.restore_point_name = restore_point_name
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The name of the snapshot.
        self.snapshot_name = snapshot_name
        # The type of the snapshot.
        # 
        # Valid values:
        # 
        # *   AUTO: automatic snapshot
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   USER: manual snapshot
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.snapshot_type = snapshot_type
        # The capacity of the source disk. Unit: GiB.
        self.source_disk_size = source_disk_size
        # The type of the source disk.
        # 
        # Valid values:
        # 
        # *   SYSTEM: system disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DATA: data disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.source_disk_type = source_disk_type
        # The status of the snapshot.
        # 
        # Valid values:
        # 
        # *   PROGRESSING: The snapshot is being created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   FAILED: The snapshot fails to be created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ACCOMPLISHED: The snapshot is created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # Indicates whether disk encryption is enabled.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key that is used when disk encryption is enabled. You can call the [ListKeys](https://help.aliyun.com/document_detail/28951.html) operation to query the list of KMS keys.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.deletion_time is not None:
            result['DeletionTime'] = self.deletion_time

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.disk_status is not None:
            result['DiskStatus'] = self.disk_status

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

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

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeletionTime') is not None:
            self.deletion_time = m.get('DeletionTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('DiskStatus') is not None:
            self.disk_status = m.get('DiskStatus')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

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

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        return self

