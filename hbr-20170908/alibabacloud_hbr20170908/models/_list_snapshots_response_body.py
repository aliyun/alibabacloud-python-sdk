# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class ListSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        snapshots: List[main_models.ListSnapshotsResponseBodySnapshots] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The return code. A value of 200 indicates success.
        self.code = code
        # The maximum number of returned results.
        self.max_results = max_results
        # The returned message. A value of successful indicates success. If an error occurs, the corresponding error message is returned.
        self.message = message
        # The token for the next page. If NextToken is empty, no more pages exist.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of backup points.
        self.snapshots = snapshots
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success
        # The total number of records.
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
        if self.code is not None:
            result['Code'] = self.code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k1 in m.get('Snapshots'):
                temp_model = main_models.ListSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_items: int = None,
        archive_time: int = None,
        backup_type: str = None,
        bytes_done: int = None,
        bytes_total: int = None,
        client_id: str = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        error_file: str = None,
        exclude: str = None,
        expire_time: int = None,
        include: str = None,
        instance_id: str = None,
        instance_name: str = None,
        items_done: int = None,
        items_total: int = None,
        job_id: str = None,
        path: str = None,
        paths: List[str] = None,
        plan_id: str = None,
        protected_data_size: int = None,
        range_end: int = None,
        range_start: int = None,
        retention: int = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        status: str = None,
        storage_class: str = None,
        table_name: str = None,
        vault_id: str = None,
    ):
        # The actual amount of data written, in bytes.
        self.actual_bytes = actual_bytes
        # The actual number of items.
        self.actual_items = actual_items
        # The archive time.
        self.archive_time = archive_time
        # The backup type. A value of **COMPLETE** indicates a full backup.
        self.backup_type = backup_type
        # The amount of backed up data, in bytes.
        self.bytes_done = bytes_done
        # The total amount of data to back up, in bytes.
        self.bytes_total = bytes_total
        # The ID of the backup client when the value of **SourceType** is **ECS_FILE** or **File**. In other cases, this parameter indicates the ID of the backup data source.
        self.client_id = client_id
        # The backup completion time. The value is a UNIX timestamp in seconds.
        self.complete_time = complete_time
        # The creation time of the backup point, in seconds.
        self.create_time = create_time
        # The backup creation time.
        self.created_time = created_time
        # The file that records backup failure information, including information about partially completed backups.
        self.error_file = error_file
        # The source paths excluded from the backup job.
        self.exclude = exclude
        # The expiration time of the backup.
        self.expire_time = expire_time
        # The source paths included in the backup job.
        self.include = include
        # The instance ID of the backup data source.
        self.instance_id = instance_id
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # The number of backed up items.
        self.items_done = items_done
        # The total number of items to back up.
        self.items_total = items_total
        # The ID of the backup job.
        self.job_id = job_id
        # The backup path.
        self.path = path
        # The list of backup paths.
        self.paths = paths
        # The ID of the backup plan.
        self.plan_id = plan_id
        # The size of the protected source data, in bytes. When the value of SourceType is ECS_FILE, this parameter indicates the capacity of the protected cloud disk.
        self.protected_data_size = protected_data_size
        # The end time of the Tablestore backup job. The value is a UNIX timestamp in milliseconds.
        self.range_end = range_end
        # The start time of the Tablestore backup job. The value is a UNIX timestamp in milliseconds.
        self.range_start = range_start
        # The retention period of the backup, in days.
        self.retention = retention
        # The hash value of the backup point.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup point.
        self.snapshot_id = snapshot_id
        # The data source type. Valid values:
        # 
        # - **ECS_FILE**: ECS file backup
        # - **File**: on-premises file backup
        # - **OSS**: OSS backup
        # - **NAS**: Alibaba Cloud NAS backup
        # - **COMMON_NAS**: on-premises NAS backup
        # - **CONTAINER**: container backup
        # - **OTS_TABLE**: Tablestore backup
        # - **COMMON_FILE_SYSTEM**: CPFS backup
        self.source_type = source_type
        # The status of the backup point. Valid values:
        self.status = status
        # The storage class. Valid values:
        self.storage_class = storage_class
        # The name of the data table in the Tablestore instance.
        self.table_name = table_name
        # The ID of the vault that stores the backup data.
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

        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items

        if self.archive_time is not None:
            result['ArchiveTime'] = self.archive_time

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

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

        if self.path is not None:
            result['Path'] = self.path

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

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

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.table_name is not None:
            result['TableName'] = self.table_name

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

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

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

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

