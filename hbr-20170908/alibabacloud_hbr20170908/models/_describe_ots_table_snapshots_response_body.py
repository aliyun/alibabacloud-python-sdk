# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeOtsTableSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        limit: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        snapshots: List[main_models.DescribeOtsTableSnapshotsResponseBodySnapshots] = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The number of backup snapshots that are displayed on the current page.
        self.limit = limit
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The backup snapshots.
        self.snapshots = snapshots
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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

        result['Snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['Snapshots'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

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

        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k1 in m.get('Snapshots'):
                temp_model = main_models.DescribeOtsTableSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeOtsTableSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        actual_bytes: str = None,
        backup_type: str = None,
        bytes_total: int = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        instance_name: str = None,
        job_id: str = None,
        parent_snapshot_hash: str = None,
        range_end: int = None,
        range_start: int = None,
        retention: int = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        start_time: int = None,
        status: str = None,
        table_name: str = None,
        updated_time: int = None,
        vault_id: str = None,
    ):
        # The actual data amount of backup snapshots after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # The time when the Tablestore instance was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # The ID of the backup job.
        self.job_id = job_id
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash
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
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS file systems
        # *   **OTS_TABLE**: backup snapshots for Tablestore instances
        self.source_type = source_type
        # The time when the backup snapshot started. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status
        # The name of the table in the Tablestore instance.
        self.table_name = table_name
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault that stores the backup snapshot.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash

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

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')

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

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

