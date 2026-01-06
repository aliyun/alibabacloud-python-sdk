# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeUdmSnapshotsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        snapshots: List[main_models.DescribeUdmSnapshotsResponseBodySnapshots] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The details about snapshots.
        self.snapshots = snapshots
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of backup snapshots.
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

        if self.message is not None:
            result['Message'] = self.message

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k1 in m.get('Snapshots'):
                temp_model = main_models.DescribeUdmSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeUdmSnapshotsResponseBodySnapshots(DaraModel):
    def __init__(
        self,
        actual_bytes: str = None,
        advanced_retention_type: str = None,
        archive_error_message: str = None,
        archive_status: str = None,
        archive_trigger_time: int = None,
        backup_type: str = None,
        bytes_total: int = None,
        can_be_deleted: bool = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        detail: main_models.DescribeUdmSnapshotsResponseBodySnapshotsDetail = None,
        disk_id: str = None,
        expire_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        native_snapshot_id: str = None,
        native_snapshot_info: str = None,
        parent_snapshot_hash: str = None,
        prefix: str = None,
        real_snapshot_time: int = None,
        retention: int = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_type: str = None,
        start_time: int = None,
        status: str = None,
        updated_time: int = None,
    ):
        # The size of the backup snapshot. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The special retention type, which is valid only for special backups. Valid values:
        # 
        # *   **WEEKLY**: weekly backups
        # *   **MONTHLY**: monthly backups
        # *   **YEARLY**: yearly backups
        self.advanced_retention_type = advanced_retention_type
        self.archive_error_message = archive_error_message
        self.archive_status = archive_status
        self.archive_trigger_time = archive_trigger_time
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The total amount of data. Unit: bytes.
        self.bytes_total = bytes_total
        # Indicates whether the disk backup point can be deleted. This parameter is valid only if the value of SourceType is UDM_ECS_DISK.
        self.can_be_deleted = can_be_deleted
        # The time when the backup snapshot was completed. The value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # The time when the backup snapshot was created.
        self.create_time = create_time
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The snapshot details.
        self.detail = detail
        # The ID of the cloud disk or local disk.
        self.disk_id = disk_id
        # The expiration time of the backup.
        self.expire_time = expire_time
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the backup job.
        self.job_id = job_id
        # The ID of the backup snapshot.
        self.native_snapshot_id = native_snapshot_id
        # The snapshot information.
        self.native_snapshot_info = native_snapshot_info
        # The hash value of the parent backup snapshot.
        self.parent_snapshot_hash = parent_snapshot_hash
        # The prefix of the backup snapshot.
        self.prefix = prefix
        # The timestamp of the backup snapshot. The value is a UNIX timestamp. Unit: seconds.
        self.real_snapshot_time = real_snapshot_time
        # The retention period of the backup snapshot. Unit: days.
        self.retention = retention
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the backup snapshot.
        self.snapshot_id = snapshot_id
        # The type of the data source. Valid values:
        # 
        # *   **UDM_ECS**: ECS instance backup
        # *   **UDM_ECS_DISK**: disk backup subtask of ECS instance backup
        # *   **UDM_DISK**: disk backup
        self.source_type = source_type
        # The time when the backup snapshot was created. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The backup job has failed.
        self.status = status
        # The time when the backup snapshot was updated. The value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes

        if self.advanced_retention_type is not None:
            result['AdvancedRetentionType'] = self.advanced_retention_type

        if self.archive_error_message is not None:
            result['ArchiveErrorMessage'] = self.archive_error_message

        if self.archive_status is not None:
            result['ArchiveStatus'] = self.archive_status

        if self.archive_trigger_time is not None:
            result['ArchiveTriggerTime'] = self.archive_trigger_time

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total

        if self.can_be_deleted is not None:
            result['CanBeDeleted'] = self.can_be_deleted

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.native_snapshot_id is not None:
            result['NativeSnapshotId'] = self.native_snapshot_id

        if self.native_snapshot_info is not None:
            result['NativeSnapshotInfo'] = self.native_snapshot_info

        if self.parent_snapshot_hash is not None:
            result['ParentSnapshotHash'] = self.parent_snapshot_hash

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.real_snapshot_time is not None:
            result['RealSnapshotTime'] = self.real_snapshot_time

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

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')

        if m.get('AdvancedRetentionType') is not None:
            self.advanced_retention_type = m.get('AdvancedRetentionType')

        if m.get('ArchiveErrorMessage') is not None:
            self.archive_error_message = m.get('ArchiveErrorMessage')

        if m.get('ArchiveStatus') is not None:
            self.archive_status = m.get('ArchiveStatus')

        if m.get('ArchiveTriggerTime') is not None:
            self.archive_trigger_time = m.get('ArchiveTriggerTime')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')

        if m.get('CanBeDeleted') is not None:
            self.can_be_deleted = m.get('CanBeDeleted')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Detail') is not None:
            temp_model = main_models.DescribeUdmSnapshotsResponseBodySnapshotsDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('NativeSnapshotId') is not None:
            self.native_snapshot_id = m.get('NativeSnapshotId')

        if m.get('NativeSnapshotInfo') is not None:
            self.native_snapshot_info = m.get('NativeSnapshotInfo')

        if m.get('ParentSnapshotHash') is not None:
            self.parent_snapshot_hash = m.get('ParentSnapshotHash')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('RealSnapshotTime') is not None:
            self.real_snapshot_time = m.get('RealSnapshotTime')

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

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class DescribeUdmSnapshotsResponseBodySnapshotsDetail(DaraModel):
    def __init__(
        self,
        consistent_level: str = None,
        contain_os_disk: bool = None,
        disk_category: str = None,
        disk_dev_name: str = None,
        disk_hbr_snapshot_id_with_device_map: Dict[str, Any] = None,
        disk_id_list: List[str] = None,
        downgrade_reason: str = None,
        host_name: str = None,
        instance_id_with_disk_id_list_map: Dict[str, Any] = None,
        instance_name: str = None,
        instance_type: str = None,
        instant_access: bool = None,
        native_snapshot_id_list: List[str] = None,
        os_disk_id: str = None,
        os_name: str = None,
        os_name_en: str = None,
        os_type: str = None,
        performance_level: str = None,
        platform: str = None,
        snapshot_group_id: str = None,
        system_disk: bool = None,
        vm_name: str = None,
    ):
        # The consistency level.
        self.consistent_level = consistent_level
        # Indicates whether the system disk is included.
        self.contain_os_disk = contain_os_disk
        # The type of the source disk.
        self.disk_category = disk_category
        # The name of the disk.
        self.disk_dev_name = disk_dev_name
        # The mapping between the device and the recovery point ID.
        self.disk_hbr_snapshot_id_with_device_map = disk_hbr_snapshot_id_with_device_map
        # The IDs of the disks that are backed up at the recovery point.
        self.disk_id_list = disk_id_list
        # The reason for the downgrade.
        self.downgrade_reason = downgrade_reason
        # The hostname.
        self.host_name = host_name
        # The mapping between the instance ID and the disk ID.
        self.instance_id_with_disk_id_list_map = instance_id_with_disk_id_list_map
        # The name of the instance.
        self.instance_name = instance_name
        # The specifications of the source instance.
        self.instance_type = instance_type
        # Indicates whether the backup is created by the instant clone feature.
        self.instant_access = instant_access
        # The list of snapshot IDs, corresponding to DiskIdList.
        self.native_snapshot_id_list = native_snapshot_id_list
        # The ID of the system disk.
        self.os_disk_id = os_disk_id
        # The name of the operating system.
        self.os_name = os_name
        # The English name of the operating system.
        self.os_name_en = os_name_en
        # The type of the operating system. Valid values: linux and windows.
        self.os_type = os_type
        # The performance level of the source disk.
        self.performance_level = performance_level
        # The system platform.
        self.platform = platform
        # The ID of the snapshot group.
        self.snapshot_group_id = snapshot_group_id
        # Indicates whether the disk is a system disk.
        self.system_disk = system_disk
        # The name of the instance.
        self.vm_name = vm_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consistent_level is not None:
            result['ConsistentLevel'] = self.consistent_level

        if self.contain_os_disk is not None:
            result['ContainOsDisk'] = self.contain_os_disk

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_dev_name is not None:
            result['DiskDevName'] = self.disk_dev_name

        if self.disk_hbr_snapshot_id_with_device_map is not None:
            result['DiskHbrSnapshotIdWithDeviceMap'] = self.disk_hbr_snapshot_id_with_device_map

        if self.disk_id_list is not None:
            result['DiskIdList'] = self.disk_id_list

        if self.downgrade_reason is not None:
            result['DowngradeReason'] = self.downgrade_reason

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_id_with_disk_id_list_map is not None:
            result['InstanceIdWithDiskIdListMap'] = self.instance_id_with_disk_id_list_map

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instant_access is not None:
            result['InstantAccess'] = self.instant_access

        if self.native_snapshot_id_list is not None:
            result['NativeSnapshotIdList'] = self.native_snapshot_id_list

        if self.os_disk_id is not None:
            result['OsDiskId'] = self.os_disk_id

        if self.os_name is not None:
            result['OsName'] = self.os_name

        if self.os_name_en is not None:
            result['OsNameEn'] = self.os_name_en

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.snapshot_group_id is not None:
            result['SnapshotGroupId'] = self.snapshot_group_id

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk

        if self.vm_name is not None:
            result['VmName'] = self.vm_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsistentLevel') is not None:
            self.consistent_level = m.get('ConsistentLevel')

        if m.get('ContainOsDisk') is not None:
            self.contain_os_disk = m.get('ContainOsDisk')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskDevName') is not None:
            self.disk_dev_name = m.get('DiskDevName')

        if m.get('DiskHbrSnapshotIdWithDeviceMap') is not None:
            self.disk_hbr_snapshot_id_with_device_map = m.get('DiskHbrSnapshotIdWithDeviceMap')

        if m.get('DiskIdList') is not None:
            self.disk_id_list = m.get('DiskIdList')

        if m.get('DowngradeReason') is not None:
            self.downgrade_reason = m.get('DowngradeReason')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceIdWithDiskIdListMap') is not None:
            self.instance_id_with_disk_id_list_map = m.get('InstanceIdWithDiskIdListMap')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstantAccess') is not None:
            self.instant_access = m.get('InstantAccess')

        if m.get('NativeSnapshotIdList') is not None:
            self.native_snapshot_id_list = m.get('NativeSnapshotIdList')

        if m.get('OsDiskId') is not None:
            self.os_disk_id = m.get('OsDiskId')

        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')

        if m.get('OsNameEn') is not None:
            self.os_name_en = m.get('OsNameEn')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SnapshotGroupId') is not None:
            self.snapshot_group_id = m.get('SnapshotGroupId')

        if m.get('SystemDisk') is not None:
            self.system_disk = m.get('SystemDisk')

        if m.get('VmName') is not None:
            self.vm_name = m.get('VmName')

        return self

