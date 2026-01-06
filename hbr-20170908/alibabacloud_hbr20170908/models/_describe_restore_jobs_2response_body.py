# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreJobs2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        restore_jobs: main_models.DescribeRestoreJobs2ResponseBodyRestoreJobs = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The response message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried restore jobs.
        self.restore_jobs = restore_jobs
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.restore_jobs:
            self.restore_jobs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restore_jobs is not None:
            result['RestoreJobs'] = self.restore_jobs.to_map()

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

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoreJobs') is not None:
            temp_model = main_models.DescribeRestoreJobs2ResponseBodyRestoreJobs()
            self.restore_jobs = temp_model.from_map(m.get('RestoreJobs'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRestoreJobs2ResponseBodyRestoreJobs(DaraModel):
    def __init__(
        self,
        restore_job: List[main_models.DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob] = None,
    ):
        self.restore_job = restore_job

    def validate(self):
        if self.restore_job:
            for v1 in self.restore_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RestoreJob'] = []
        if self.restore_job is not None:
            for k1 in self.restore_job:
                result['RestoreJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_job = []
        if m.get('RestoreJob') is not None:
            for k1 in m.get('RestoreJob'):
                temp_model = main_models.DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob()
                self.restore_job.append(temp_model.from_map(k1))

        return self

class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJob(DaraModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_items: int = None,
        bytes_done: int = None,
        bytes_total: int = None,
        cluster_id: str = None,
        complete_time: int = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        error_file: str = None,
        error_message: str = None,
        exclude: str = None,
        expire_time: int = None,
        failback_detail: str = None,
        include: str = None,
        items_done: int = None,
        items_total: int = None,
        metering_bytes_done: int = None,
        metering_bytes_total: int = None,
        options: str = None,
        ots_detail: main_models.DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail = None,
        parent_id: str = None,
        progress: int = None,
        report: main_models.DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport = None,
        restore_id: str = None,
        restore_type: str = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        source_instance_id: str = None,
        source_type: str = None,
        speed: int = None,
        start_time: int = None,
        status: str = None,
        storage_class: str = None,
        target_bucket: str = None,
        target_client_id: str = None,
        target_create_time: int = None,
        target_data_source_id: str = None,
        target_file_system_id: str = None,
        target_instance_id: str = None,
        target_instance_name: str = None,
        target_path: str = None,
        target_prefix: str = None,
        target_table_name: str = None,
        target_time: int = None,
        udm_detail: str = None,
        updated_time: int = None,
        vault_id: str = None,
    ):
        # The actual amount of data that is restored after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the actual number of objects that are restored by the restore job.
        self.actual_items = actual_items
        # The amount of data that was restored. Unit: bytes.
        self.bytes_done = bytes_done
        # The total amount of data that was backed up from the data source. Unit: bytes.
        self.bytes_total = bytes_total
        # The ID of the client group used for restoration.
        self.cluster_id = cluster_id
        # The time when the restore job was completed. This value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # The time when the restore job was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Indicates whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The files that failed to be restored.
        self.error_file = error_file
        # The error message that is returned for the restore job.
        self.error_message = error_message
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the paths to the files that are excluded from the restore job. The value can be up to 255 characters in length.
        self.exclude = exclude
        # The time when the restore job expires.
        self.expire_time = expire_time
        # The details about the VMware failback task.
        self.failback_detail = failback_detail
        # The paths to the files that are included in the restore job.
        self.include = include
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the number of restored objects.
        self.items_done = items_done
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the total number of objects in the data source.
        self.items_total = items_total
        # The amount of data that was restored. Unit: bytes. This parameter is valid only if the StorageClass parameter is set to ARCHIVE. The minimum billable size of the data stored at the Archive tier is 1 MB.
        self.metering_bytes_done = metering_bytes_done
        # The total amount of data that was backed up from the data source. Unit: bytes. This parameter is valid only if the StorageClass parameter is set to ARCHIVE. The minimum billable size of the data stored at the Archive tier is 1 MB.
        self.metering_bytes_total = metering_bytes_total
        # This parameter is valid only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates whether Windows Volume Shadow Copy Service (VSS) is used to define a restoration path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before you can set this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot restore data from multiple directories.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # The ID of the parent job.
        self.parent_id = parent_id
        # The progress of the restore job. Valid values: [0,10000]. For example, 10000 indicates that the progress is 100%.
        self.progress = progress
        # The report of the restore job.
        self.report = report
        # The ID of the restore job.
        self.restore_id = restore_id
        # The type of the restore job.
        self.restore_type = restore_type
        # The hash value of the backup snapshot.
        self.snapshot_hash = snapshot_hash
        # The ID of the snapshot used for restoration.
        self.snapshot_id = snapshot_id
        self.source_instance_id = source_instance_id
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS (NAS) file systems
        # *   **OTS_TABLE**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        self.source_type = source_type
        # The average speed at which data is backed up. Unit: KB/s.
        self.speed = speed
        # The time when the restore job started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the restore job. Valid values:
        # 
        # *   **COMPLETE**: The job is completed.
        # *   **PARTIAL_COMPLETE**: The job is partially completed.
        # *   **FAILED**: The job failed.
        self.status = status
        # The storage class of the backup data. Valid values:
        # 
        # *   **STANDARD**
        # *   **ARCHIVE**
        self.storage_class = storage_class
        # The name of the destination OSS bucket. This parameter is returned only for OSS buckets.
        self.target_bucket = target_bucket
        # The ID of the destination client.
        self.target_client_id = target_client_id
        # The time when the file system was created. This parameter is returned only for NAS file systems.
        self.target_create_time = target_create_time
        # The ID of the destination data source.
        self.target_data_source_id = target_data_source_id
        # The ID of the destination NAS file system. This parameter is returned only for NAS file systems.
        self.target_file_system_id = target_file_system_id
        # The ID of the destination instance for the restore job.
        self.target_instance_id = target_instance_id
        # The name of the destination Tablestore instance.
        self.target_instance_name = target_instance_name
        # The destination file path of the restore job.
        self.target_path = target_path
        # The prefix of the objects that are restored. This parameter is returned only for OSS buckets.
        self.target_prefix = target_prefix
        # The name of the destination table in the Tablestore instance.
        self.target_table_name = target_table_name
        # The time when the Tablestore instance was backed up. This value is a UNIX timestamp. Unit: seconds.
        self.target_time = target_time
        # The details about Elastic Compute Service (ECS) instance backup.
        self.udm_detail = udm_detail
        # The time when the restore job was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.ots_detail:
            self.ots_detail.validate()
        if self.report:
            self.report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes

        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items

        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done

        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.error_file is not None:
            result['ErrorFile'] = self.error_file

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.failback_detail is not None:
            result['FailbackDetail'] = self.failback_detail

        if self.include is not None:
            result['Include'] = self.include

        if self.items_done is not None:
            result['ItemsDone'] = self.items_done

        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total

        if self.metering_bytes_done is not None:
            result['MeteringBytesDone'] = self.metering_bytes_done

        if self.metering_bytes_total is not None:
            result['MeteringBytesTotal'] = self.metering_bytes_total

        if self.options is not None:
            result['Options'] = self.options

        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.report is not None:
            result['Report'] = self.report.to_map()

        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket

        if self.target_client_id is not None:
            result['TargetClientId'] = self.target_client_id

        if self.target_create_time is not None:
            result['TargetCreateTime'] = self.target_create_time

        if self.target_data_source_id is not None:
            result['TargetDataSourceId'] = self.target_data_source_id

        if self.target_file_system_id is not None:
            result['TargetFileSystemId'] = self.target_file_system_id

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        if self.target_prefix is not None:
            result['TargetPrefix'] = self.target_prefix

        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name

        if self.target_time is not None:
            result['TargetTime'] = self.target_time

        if self.udm_detail is not None:
            result['UdmDetail'] = self.udm_detail

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')

        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')

        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')

        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('ErrorFile') is not None:
            self.error_file = m.get('ErrorFile')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FailbackDetail') is not None:
            self.failback_detail = m.get('FailbackDetail')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')

        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')

        if m.get('MeteringBytesDone') is not None:
            self.metering_bytes_done = m.get('MeteringBytesDone')

        if m.get('MeteringBytesTotal') is not None:
            self.metering_bytes_total = m.get('MeteringBytesTotal')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('OtsDetail') is not None:
            temp_model = main_models.DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail()
            self.ots_detail = temp_model.from_map(m.get('OtsDetail'))

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Report') is not None:
            temp_model = main_models.DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport()
            self.report = temp_model.from_map(m.get('Report'))

        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')

        if m.get('TargetClientId') is not None:
            self.target_client_id = m.get('TargetClientId')

        if m.get('TargetCreateTime') is not None:
            self.target_create_time = m.get('TargetCreateTime')

        if m.get('TargetDataSourceId') is not None:
            self.target_data_source_id = m.get('TargetDataSourceId')

        if m.get('TargetFileSystemId') is not None:
            self.target_file_system_id = m.get('TargetFileSystemId')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        if m.get('TargetPrefix') is not None:
            self.target_prefix = m.get('TargetPrefix')

        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')

        if m.get('TargetTime') is not None:
            self.target_time = m.get('TargetTime')

        if m.get('UdmDetail') is not None:
            self.udm_detail = m.get('UdmDetail')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobReport(DaraModel):
    def __init__(
        self,
        failed_files: str = None,
        report_task_status: str = None,
        skipped_files: str = None,
        success_files: str = None,
        total_files: str = None,
    ):
        # The files that failed to be executed.
        self.failed_files = failed_files
        # The status of the report generation.
        self.report_task_status = report_task_status
        # The skipped files.
        self.skipped_files = skipped_files
        # The files that are successfully executed.
        self.success_files = success_files
        # The full files that are restored based on the file list.
        self.total_files = total_files

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_files is not None:
            result['FailedFiles'] = self.failed_files

        if self.report_task_status is not None:
            result['ReportTaskStatus'] = self.report_task_status

        if self.skipped_files is not None:
            result['SkippedFiles'] = self.skipped_files

        if self.success_files is not None:
            result['SuccessFiles'] = self.success_files

        if self.total_files is not None:
            result['TotalFiles'] = self.total_files

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedFiles') is not None:
            self.failed_files = m.get('FailedFiles')

        if m.get('ReportTaskStatus') is not None:
            self.report_task_status = m.get('ReportTaskStatus')

        if m.get('SkippedFiles') is not None:
            self.skipped_files = m.get('SkippedFiles')

        if m.get('SuccessFiles') is not None:
            self.success_files = m.get('SuccessFiles')

        if m.get('TotalFiles') is not None:
            self.total_files = m.get('TotalFiles')

        return self

class DescribeRestoreJobs2ResponseBodyRestoreJobsRestoreJobOtsDetail(DaraModel):
    def __init__(
        self,
        batch_channel_count: int = None,
        overwrite_existing: bool = None,
    ):
        # The number of channels processed by each Tablestore restore job.
        self.batch_channel_count = batch_channel_count
        # Indicates whether the existing Tablestore restore job was overwritten.
        self.overwrite_existing = overwrite_existing

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_channel_count is not None:
            result['BatchChannelCount'] = self.batch_channel_count

        if self.overwrite_existing is not None:
            result['OverwriteExisting'] = self.overwrite_existing

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchChannelCount') is not None:
            self.batch_channel_count = m.get('BatchChannelCount')

        if m.get('OverwriteExisting') is not None:
            self.overwrite_existing = m.get('OverwriteExisting')

        return self

