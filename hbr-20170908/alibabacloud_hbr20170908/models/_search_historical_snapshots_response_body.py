# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class SearchHistoricalSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        limit: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        snapshots: main_models.SearchHistoricalSnapshotsResponseBodySnapshots = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The number of historical backup snapshots that are displayed on the current page.
        self.limit = limit
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The historical backup snapshots.
        self.snapshots = snapshots
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned backup snapshots that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Snapshots') is not None:
            temp_model = main_models.SearchHistoricalSnapshotsResponseBodySnapshots()
            self.snapshots = temp_model.from_map(m.get('Snapshots'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchHistoricalSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        snapshot: List[main_models.SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot] = None,
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
                temp_model = main_models.SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k1))

        return self

class SearchHistoricalSnapshotsResponseBodySnapshotsSnapshot(DaraModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_items: int = None,
        archive_time: int = None,
        backup_type: str = None,
        bucket: str = None,
        bytes_done: int = None,
        bytes_total: int = None,
        client_id: str = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        error_file: str = None,
        exclude: str = None,
        expire_time: int = None,
        file_system_id: str = None,
        include: str = None,
        instance_id: str = None,
        instance_name: str = None,
        items_done: int = None,
        items_total: int = None,
        job_id: str = None,
        parent_snapshot_hash: str = None,
        path: str = None,
        paths: main_models.SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths = None,
        prefix: str = None,
        protected_data_size: int = None,
        range_end: int = None,
        range_start: int = None,
        retention: int = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_parent_snapshot_hash: str = None,
        source_snapshot_hash: str = None,
        source_type: str = None,
        start_time: int = None,
        status: str = None,
        storage_class: str = None,
        table_name: str = None,
        updated_time: int = None,
        use_common_nas: bool = None,
        vault_id: str = None,
    ):
        # The actual data amount of backup snapshots after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The actual number of backup snapshots.
        # 
        # >  This parameter is available only for file backup.
        self.actual_items = actual_items
        # Time to archive
        self.archive_time = archive_time
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the name of the OSS bucket.
        self.bucket = bucket
        # The actual amount of data that is generated by incremental backups. Unit: bytes.
        self.bytes_done = bytes_done
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the ID of the HBR client.
        self.client_id = client_id
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the time when the file system was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The files that record the information about backup failures, including the information about partially completed backups.
        self.error_file = error_file
        # Backup paths not included in the backup job.
        self.exclude = exclude
        # The time when the snapshot expired. The value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the ID of the NAS file system.
        self.file_system_id = file_system_id
        # Backup paths included in the backup job.
        self.include = include
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # The number of objects that are backed up.
        # 
        # >  This parameter is available only for file backup.
        self.items_done = items_done
        # The total number of objects in the data source.
        # 
        # >  This parameter is available only for file backup.
        self.items_total = items_total
        # The ID of the backup job.
        self.job_id = job_id
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the path to the files that are backed up.
        self.path = path
        # The source paths.
        self.paths = paths
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the prefix of objects that are backed up.
        self.prefix = prefix
        self.protected_data_size = protected_data_size
        # The time when the backup job ended. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_end = range_end
        # The time when the backup job started. The value is a UNIX timestamp. Unit: milliseconds.
        self.range_start = range_start
        # The retention period of the backup snapshot. Unit: days.
        self.retention = retention
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # Parent snapshot HASH value before archiving.
        self.source_parent_snapshot_hash = source_parent_snapshot_hash
        # Snapshot HASH value before archiving
        self.source_snapshot_hash = source_snapshot_hash
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for ECS files
        # *   **OSS**: backup snapshots for OSS buckets
        # *   **NAS**: backup snapshots for NAS file systems
        self.source_type = source_type
        # The time when the backup snapshot started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status
        # Storage type. Values: 
        # - **Standard**: Standard. 
        # - **Archive**: Archive. 
        # - **ColdArchive**: Cold Archive.
        self.storage_class = storage_class
        # The name of a table in the Tablestore instance.
        self.table_name = table_name
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # Whether to use local NAS.
        self.use_common_nas = use_common_nas
        # The ID of the backup vault that stores the backup snapshot.
        self.vault_id = vault_id

    def validate(self):
        if self.paths:
            self.paths.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes

        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items

        if self.archive_time is not None:
            result['ArchiveTime'] = self.archive_time

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done

        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.error_file is not None:
            result['ErrorFile'] = self.error_file

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.include is not None:
            result['Include'] = self.include

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.items_done is not None:
            result['ItemsDone'] = self.items_done

        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash

        if self.path is not None:
            result['Path'] = self.path

        if self.paths is not None:
            result['Paths'] = self.paths.to_map()

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.protected_data_size is not None:
            result['ProtectedDataSize'] = self.protected_data_size

        if self.range_end is not None:
            result['RangeEnd'] = self.range_end

        if self.range_start is not None:
            result['RangeStart'] = self.range_start

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.source_parent_snapshot_hash is not None:
            result['SourceParentSnapshotHash'] = self.source_parent_snapshot_hash

        if self.source_snapshot_hash is not None:
            result['SourceSnapshotHash'] = self.source_snapshot_hash

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.use_common_nas is not None:
            result['UseCommonNas'] = self.use_common_nas

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')

        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')

        if m.get('ArchiveTime') is not None:
            self.archive_time = m.get('ArchiveTime')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')

        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ErrorFile') is not None:
            self.error_file = m.get('ErrorFile')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')

        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Paths') is not None:
            temp_model = main_models.SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths()
            self.paths = temp_model.from_map(m.get('Paths'))

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('ProtectedDataSize') is not None:
            self.protected_data_size = m.get('ProtectedDataSize')

        if m.get('RangeEnd') is not None:
            self.range_end = m.get('RangeEnd')

        if m.get('RangeStart') is not None:
            self.range_start = m.get('RangeStart')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SourceParentSnapshotHash') is not None:
            self.source_parent_snapshot_hash = m.get('SourceParentSnapshotHash')

        if m.get('SourceSnapshotHash') is not None:
            self.source_snapshot_hash = m.get('SourceSnapshotHash')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('UseCommonNas') is not None:
            self.use_common_nas = m.get('UseCommonNas')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class SearchHistoricalSnapshotsResponseBodySnapshotsSnapshotPaths(DaraModel):
    def __init__(
        self,
        path: List[str] = None,
    ):
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

