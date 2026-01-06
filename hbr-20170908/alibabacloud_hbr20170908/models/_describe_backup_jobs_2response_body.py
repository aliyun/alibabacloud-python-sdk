# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupJobs2ResponseBody(DaraModel):
    def __init__(
        self,
        backup_jobs: main_models.DescribeBackupJobs2ResponseBodyBackupJobs = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The returned backup jobs that meet the specified conditions.
        self.backup_jobs = backup_jobs
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful.
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned backup jobs that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.backup_jobs:
            self.backup_jobs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_jobs is not None:
            result['BackupJobs'] = self.backup_jobs.to_map()

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

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupJobs') is not None:
            temp_model = main_models.DescribeBackupJobs2ResponseBodyBackupJobs()
            self.backup_jobs = temp_model.from_map(m.get('BackupJobs'))

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

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBackupJobs2ResponseBodyBackupJobs(DaraModel):
    def __init__(
        self,
        backup_job: List[main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJob] = None,
    ):
        self.backup_job = backup_job

    def validate(self):
        if self.backup_job:
            for v1 in self.backup_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupJob'] = []
        if self.backup_job is not None:
            for k1 in self.backup_job:
                result['BackupJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_job = []
        if m.get('BackupJob') is not None:
            for k1 in m.get('BackupJob'):
                temp_model = main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJob()
                self.backup_job.append(temp_model.from_map(k1))

        return self

class DescribeBackupJobs2ResponseBodyBackupJobsBackupJob(DaraModel):
    def __init__(
        self,
        actual_bytes: int = None,
        actual_files: int = None,
        actual_items: int = None,
        backup_type: str = None,
        bucket: str = None,
        bytes_done: int = None,
        bytes_total: int = None,
        change_list_path: str = None,
        client_id: str = None,
        complete_time: int = None,
        create_time: int = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        dest_data_source_detail: str = None,
        dest_data_source_id: str = None,
        dest_source_type: str = None,
        detail: main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail = None,
        error_message: str = None,
        exclude: str = None,
        file_system_id: str = None,
        files_done: int = None,
        files_total: int = None,
        identifier: str = None,
        include: str = None,
        instance_id: str = None,
        instance_name: str = None,
        items_done: int = None,
        items_total: int = None,
        job_id: str = None,
        job_name: str = None,
        options: str = None,
        ots_detail: main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail = None,
        paths: main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths = None,
        plan_id: str = None,
        prefix: str = None,
        progress: int = None,
        report: main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobReport = None,
        source_type: str = None,
        speed: int = None,
        speed_limit: str = None,
        start_time: int = None,
        status: str = None,
        table_name: str = None,
        updated_time: int = None,
        vault_id: str = None,
    ):
        # The actual amount of data that is backed up after duplicates are removed. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The number of files that are actually processed.
        self.actual_files = actual_files
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the actual number of objects that are backed up by the backup job.
        self.actual_items = actual_items
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the name of the OSS bucket that is backed up.
        self.bucket = bucket
        # The actual amount of data that is generated by incremental backups. Unit: bytes.
        self.bytes_done = bytes_done
        # The total amount of data that is backed up from the data source. Unit: bytes.
        self.bytes_total = bytes_total
        # The data source details at the destination. Thisparameter is returned only for data synchronization.
        self.change_list_path = change_list_path
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the ID of the backup client.
        self.client_id = client_id
        # The time when the backup job was completed. This value is a UNIX timestamp. Unit: seconds.
        self.complete_time = complete_time
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the time when the file system was created. This value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The time when the backup job was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the RAM role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Specifies whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT: Data is backed up within the same Alibaba Cloud account.
        # *   CROSS_ACCOUNT: Data is backed up across Alibaba Cloud accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # Destination data source details. (Required only for synchronization)
        self.dest_data_source_detail = dest_data_source_detail
        # Destination data source ID. (Required only for synchronization)
        self.dest_data_source_id = dest_data_source_id
        # Destination data source type. (Required only for synchronization)
        self.dest_source_type = dest_source_type
        # The udm backup job detail.
        self.detail = detail
        # The error message that is returned for the backup job.
        self.error_message = error_message
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the paths to the files that are excluded from the backup job. The value must be 1 to 255 characters in length.
        self.exclude = exclude
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the ID of the NAS file system.
        self.file_system_id = file_system_id
        # The number of files that have been processed.
        self.files_done = files_done
        # The total number of files to be processed.
        self.files_total = files_total
        # The identifier of the container cluster. For a Container Service for Kubernetes (ACK) cluster, specify the cluster ID.
        self.identifier = identifier
        # The paths to the files that are included in the backup job.
        self.include = include
        # This parameter is returned only if the **SourceType** parameter is set to **NAS**. This parameter indicates the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the number of objects that are backed up.
        self.items_done = items_done
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the total number of objects in the data source.
        self.items_total = items_total
        # The ID of the backup job.
        self.job_id = job_id
        # The name of the backup job.
        self.job_name = job_name
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates whether Windows VSS is used to define a backup path.
        # 
        # *   This parameter is available only for Windows ECS instances.
        # *   If data changes occur in the backup source, the source data must be the same as the data to be backed up before the system sets this parameter to `["UseVSS":true]`.
        # *   If you use VSS, you cannot back up data from multiple directories.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # The backup paths.
        self.paths = paths
        # The ID of the backup plan.
        self.plan_id = plan_id
        # This parameter is returned only if the **SourceType** parameter is set to **OSS**. This parameter indicates the prefix of objects that are backed up.
        self.prefix = prefix
        # The backup progress. For example, 10000 indicates that the progress is 100%.
        self.progress = progress
        # Task Report
        self.report = report
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: OSS buckets
        # *   **NAS**: NAS file systems
        self.source_type = source_type
        # The average speed at which data is backed up. Unit: KB/s.
        self.speed = speed
        # This parameter is returned only if the **SourceType** parameter is set to **ECS_FILE**. This parameter indicates the throttling rules. Format: `{start}{end}{bandwidth}`. Multiple throttling rules are separated with vertical bars (`{start}|{end}|{bandwidth}`). A specified time range cannot overlap with another one.
        # 
        # *   **start**: the start hour
        # *   **end**: the end hour
        # *   **bandwidth**: the bandwidth. Unit: KB/s.
        self.speed_limit = speed_limit
        # The time when the backup job started. This value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time
        # The status of the backup job. Valid values:
        # 
        # *   **COMPLETE**: The backup job is completed.
        # *   **PARTIAL_COMPLETE**: The backup job is partially completed.
        # *   **FAILED**: The restore job has failed.
        self.status = status
        # The name of a destination table in the Tablestore instance.
        self.table_name = table_name
        # The time when the backup job was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.detail:
            self.detail.validate()
        if self.ots_detail:
            self.ots_detail.validate()
        if self.paths:
            self.paths.validate()
        if self.report:
            self.report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes

        if self.actual_files is not None:
            result['ActualFiles'] = self.actual_files

        if self.actual_items is not None:
            result['ActualItems'] = self.actual_items

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done

        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total

        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.dest_data_source_detail is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail

        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id

        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.files_done is not None:
            result['FilesDone'] = self.files_done

        if self.files_total is not None:
            result['FilesTotal'] = self.files_total

        if self.identifier is not None:
            result['Identifier'] = self.identifier

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

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.options is not None:
            result['Options'] = self.options

        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()

        if self.paths is not None:
            result['Paths'] = self.paths.to_map()

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.report is not None:
            result['Report'] = self.report.to_map()

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

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

        if m.get('ActualFiles') is not None:
            self.actual_files = m.get('ActualFiles')

        if m.get('ActualItems') is not None:
            self.actual_items = m.get('ActualItems')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')

        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')

        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail = m.get('DestDataSourceDetail')

        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')

        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')

        if m.get('Detail') is not None:
            temp_model = main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FilesDone') is not None:
            self.files_done = m.get('FilesDone')

        if m.get('FilesTotal') is not None:
            self.files_total = m.get('FilesTotal')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

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

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('OtsDetail') is not None:
            temp_model = main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail()
            self.ots_detail = temp_model.from_map(m.get('OtsDetail'))

        if m.get('Paths') is not None:
            temp_model = main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths()
            self.paths = temp_model.from_map(m.get('Paths'))

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Report') is not None:
            temp_model = main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobReport()
            self.report = temp_model.from_map(m.get('Report'))

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

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

class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobReport(DaraModel):
    def __init__(
        self,
        failed_files: str = None,
        report_task_status: str = None,
        skipped_files: str = None,
        success_files: str = None,
        total_files: str = None,
    ):
        # List of failed files
        self.failed_files = failed_files
        # Report generation status.
        self.report_task_status = report_task_status
        # List of skipped files
        self.skipped_files = skipped_files
        # List of successful files.
        self.success_files = success_files
        # List of all files. (This field is not returned for data synchronization)
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

class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobPaths(DaraModel):
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

class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetail(DaraModel):
    def __init__(
        self,
        table_names: main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames = None,
    ):
        # The names of the destination tables in the Tablestore instance.
        self.table_names = table_names

    def validate(self):
        if self.table_names:
            self.table_names.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_names is not None:
            result['TableNames'] = self.table_names.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableNames') is not None:
            temp_model = main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames()
            self.table_names = temp_model.from_map(m.get('TableNames'))

        return self

class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobOtsDetailTableNames(DaraModel):
    def __init__(
        self,
        table_name: List[str] = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetail(DaraModel):
    def __init__(
        self,
        destination_native_snapshot_error_message: str = None,
        destination_native_snapshot_id: str = None,
        destination_native_snapshot_progress: int = None,
        destination_native_snapshot_status: str = None,
        destination_retention: int = None,
        destination_snapshot_id: str = None,
        disk_native_snapshot_id_list: main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList = None,
        do_copy: bool = None,
        instance_infos: Dict[str, Any] = None,
        native_snapshot_id: str = None,
    ):
        # The information about the remote replication failure.
        self.destination_native_snapshot_error_message = destination_native_snapshot_error_message
        # The ID of the remote replication snapshot.
        self.destination_native_snapshot_id = destination_native_snapshot_id
        # The progress of the remote replication.
        self.destination_native_snapshot_progress = destination_native_snapshot_progress
        # The state of the remote replication.
        self.destination_native_snapshot_status = destination_native_snapshot_status
        # The retention period of the remote replication backup.
        self.destination_retention = destination_retention
        # The ID of the remote replication backup.
        self.destination_snapshot_id = destination_snapshot_id
        # The mapping between snapshots and disks.
        self.disk_native_snapshot_id_list = disk_native_snapshot_id_list
        # Indicates whether remote replication is enabled.
        self.do_copy = do_copy
        # The ecs instance infos.
        self.instance_infos = instance_infos
        # The ID of the backup snapshot.
        self.native_snapshot_id = native_snapshot_id

    def validate(self):
        if self.disk_native_snapshot_id_list:
            self.disk_native_snapshot_id_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_native_snapshot_error_message is not None:
            result['DestinationNativeSnapshotErrorMessage'] = self.destination_native_snapshot_error_message

        if self.destination_native_snapshot_id is not None:
            result['DestinationNativeSnapshotId'] = self.destination_native_snapshot_id

        if self.destination_native_snapshot_progress is not None:
            result['DestinationNativeSnapshotProgress'] = self.destination_native_snapshot_progress

        if self.destination_native_snapshot_status is not None:
            result['DestinationNativeSnapshotStatus'] = self.destination_native_snapshot_status

        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention

        if self.destination_snapshot_id is not None:
            result['DestinationSnapshotId'] = self.destination_snapshot_id

        if self.disk_native_snapshot_id_list is not None:
            result['DiskNativeSnapshotIdList'] = self.disk_native_snapshot_id_list.to_map()

        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy

        if self.instance_infos is not None:
            result['InstanceInfos'] = self.instance_infos

        if self.native_snapshot_id is not None:
            result['NativeSnapshotId'] = self.native_snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationNativeSnapshotErrorMessage') is not None:
            self.destination_native_snapshot_error_message = m.get('DestinationNativeSnapshotErrorMessage')

        if m.get('DestinationNativeSnapshotId') is not None:
            self.destination_native_snapshot_id = m.get('DestinationNativeSnapshotId')

        if m.get('DestinationNativeSnapshotProgress') is not None:
            self.destination_native_snapshot_progress = m.get('DestinationNativeSnapshotProgress')

        if m.get('DestinationNativeSnapshotStatus') is not None:
            self.destination_native_snapshot_status = m.get('DestinationNativeSnapshotStatus')

        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')

        if m.get('DestinationSnapshotId') is not None:
            self.destination_snapshot_id = m.get('DestinationSnapshotId')

        if m.get('DiskNativeSnapshotIdList') is not None:
            temp_model = main_models.DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList()
            self.disk_native_snapshot_id_list = temp_model.from_map(m.get('DiskNativeSnapshotIdList'))

        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')

        if m.get('InstanceInfos') is not None:
            self.instance_infos = m.get('InstanceInfos')

        if m.get('NativeSnapshotId') is not None:
            self.native_snapshot_id = m.get('NativeSnapshotId')

        return self

class DescribeBackupJobs2ResponseBodyBackupJobsBackupJobDetailDiskNativeSnapshotIdList(DaraModel):
    def __init__(
        self,
        disk_native_snapshot_id: List[str] = None,
    ):
        self.disk_native_snapshot_id = disk_native_snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_native_snapshot_id is not None:
            result['DiskNativeSnapshotId'] = self.disk_native_snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskNativeSnapshotId') is not None:
            self.disk_native_snapshot_id = m.get('DiskNativeSnapshotId')

        return self

