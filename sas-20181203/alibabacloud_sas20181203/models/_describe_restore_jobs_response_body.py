# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreJobsResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeRestoreJobsResponseBodyPageInfo = None,
        request_id: str = None,
        restore_jobs: List[main_models.DescribeRestoreJobsResponseBodyRestoreJobs] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The details about the restoration tasks.
        self.restore_jobs = restore_jobs

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.restore_jobs:
            for v1 in self.restore_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RestoreJobs'] = []
        if self.restore_jobs is not None:
            for k1 in self.restore_jobs:
                result['RestoreJobs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeRestoreJobsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.restore_jobs = []
        if m.get('RestoreJobs') is not None:
            for k1 in m.get('RestoreJobs'):
                temp_model = main_models.DescribeRestoreJobsResponseBodyRestoreJobs()
                self.restore_jobs.append(temp_model.from_map(k1))

        return self

class DescribeRestoreJobsResponseBodyRestoreJobs(DaraModel):
    def __init__(
        self,
        actual_bytes: int = None,
        bytes_done: int = None,
        bytes_total: int = None,
        client_id: str = None,
        complete_time: int = None,
        created_time: int = None,
        duration: int = None,
        error_count: int = None,
        error_file: str = None,
        error_file_url: str = None,
        error_type: str = None,
        eta: int = None,
        excludes: str = None,
        exit_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        includes: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        items_done: int = None,
        items_total: int = None,
        message: str = None,
        percentage: int = None,
        request_id: str = None,
        restore_id: str = None,
        restore_name: str = None,
        restore_type: str = None,
        snapshot_hash: str = None,
        snapshot_id: str = None,
        snapshot_version: str = None,
        source: str = None,
        source_client_id: str = None,
        speed: int = None,
        status: str = None,
        target: str = None,
        updated_time: int = None,
        uuid: str = None,
        vault_id: str = None,
        vault_region_id: str = None,
    ):
        # The size of backup data. Unit: bytes.
        self.actual_bytes = actual_bytes
        # The total size of data that is restored. Unit: bytes.
        self.bytes_done = bytes_done
        # The total size of data that you want to restore. Unit: bytes.
        self.bytes_total = bytes_total
        # The ID of the anti-ransomware agent that is used to perform the restoration task.
        self.client_id = client_id
        # The timestamp when the restoration task is complete. Unit: milliseconds.
        self.complete_time = complete_time
        # The timestamp when the restoration task is created. Unit: milliseconds.
        self.created_time = created_time
        # The duration of the restoration task. Unit: seconds.
        self.duration = duration
        # The number of the restoration tasks on which errors occur.
        self.error_count = error_count
        # The name of the CSV file. The CSV file contains the files that fail to be restored.
        self.error_file = error_file
        # The URL to download the CSV file. The CSV file contains the files that fail to be restored.
        self.error_file_url = error_file_url
        # The error code that is returned for the restoration task.
        self.error_type = error_type
        # The timestamp when the in-progress restoration task is expected to be complete. Unit: seconds.
        self.eta = eta
        # The directory excluded from the anti-ransomware policy. The value is the directory that you specify to skip protection when you create the anti-ransomware policy.
        self.excludes = excludes
        # The return value of the restoration task.
        self.exit_code = exit_code
        # The time when the restoration task is created.
        self.gmt_create = gmt_create
        # The time when the restoration task is updated.
        self.gmt_modified = gmt_modified
        # The directory in which the restored file is stored. The value is the directory that you specify for protection when you create the anti-ransomware policy
        self.includes = includes
        # The ID of the server whose data you want to restore.
        self.instance_id = instance_id
        # The name of the server whose data you want to restore.
        self.instance_name = instance_name
        # The public IP address of the server whose data you want to restore.
        self.internet_ip = internet_ip
        # The internal IP address of the server whose data you want to restore.
        self.intranet_ip = intranet_ip
        # The number of files that are restored.
        self.items_done = items_done
        # The total number of files that need to be restored.
        self.items_total = items_total
        # The error message.
        self.message = message
        # The progress of the restoration task in percentage.
        self.percentage = percentage
        # The request ID.
        self.request_id = request_id
        # The ID of the restoration task.
        self.restore_id = restore_id
        # The name of the restoration task.
        self.restore_name = restore_name
        # The type of the file that is restored. Valid values:
        # 
        # *   **ECS_FILE**: files on Elastic Compute Service (ECS) instances
        # *   **FILE**: files on servers in data centers
        self.restore_type = restore_type
        # The hash value of the snapshot that stores backup data when the data is backed up.
        self.snapshot_hash = snapshot_hash
        # The hash value ID of the snapshot that stores backup data when the data is backed up.
        self.snapshot_id = snapshot_id
        # The version of the backup data.
        self.snapshot_version = snapshot_version
        # The restored content.
        self.source = source
        # The ID of the anti-ransomware agent that is used to back up data.
        self.source_client_id = source_client_id
        # The speed at which data is restored. Unit: byte/s.
        self.speed = speed
        # The status of the restoration task. Valid values:
        # 
        # *   **RUNNING**: The task is running.
        # *   **COMPLETE**: The task is complete.
        # *   **FAILED**: The task fails.
        # *   **CANCELING**: The task is being canceled.
        # *   **CANCELED**: The task is canceled.
        # *   **PARTIAL_COMPLETE**: The task is partially successful.
        # *   **CREATED**: The task was created but is not run.
        # *   **EXPIRED**: The task is not updated.
        # *   **QUEUED**: The task is waiting to be run.
        # *   **CLIENT_DELETED**: The task fails because the anti-ransomware agent is uninstalled.
        self.status = status
        # The folder to which the backup data is restored. After you create the restoration task, the backup data is restored to the specified folder.
        self.target = target
        # The timestamp when the restoration task was last updated. Unit: milliseconds.
        self.updated_time = updated_time
        # The UUID of the server whose data you want to restore.
        self.uuid = uuid
        # The ID of the backup vault in which the backup data is stored.
        self.vault_id = vault_id
        # The ID of the region where the backup vault resides.
        self.vault_region_id = vault_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes

        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done

        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.error_file is not None:
            result['ErrorFile'] = self.error_file

        if self.error_file_url is not None:
            result['ErrorFileUrl'] = self.error_file_url

        if self.error_type is not None:
            result['ErrorType'] = self.error_type

        if self.eta is not None:
            result['Eta'] = self.eta

        if self.excludes is not None:
            result['Excludes'] = self.excludes

        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.includes is not None:
            result['Includes'] = self.includes

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.items_done is not None:
            result['ItemsDone'] = self.items_done

        if self.items_total is not None:
            result['ItemsTotal'] = self.items_total

        if self.message is not None:
            result['Message'] = self.message

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id

        if self.restore_name is not None:
            result['RestoreName'] = self.restore_name

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        if self.snapshot_hash is not None:
            result['SnapshotHash'] = self.snapshot_hash

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_version is not None:
            result['SnapshotVersion'] = self.snapshot_version

        if self.source is not None:
            result['Source'] = self.source

        if self.source_client_id is not None:
            result['SourceClientId'] = self.source_client_id

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.status is not None:
            result['Status'] = self.status

        if self.target is not None:
            result['Target'] = self.target

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        if self.vault_region_id is not None:
            result['VaultRegionId'] = self.vault_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')

        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')

        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('ErrorFile') is not None:
            self.error_file = m.get('ErrorFile')

        if m.get('ErrorFileUrl') is not None:
            self.error_file_url = m.get('ErrorFileUrl')

        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')

        if m.get('Eta') is not None:
            self.eta = m.get('Eta')

        if m.get('Excludes') is not None:
            self.excludes = m.get('Excludes')

        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Includes') is not None:
            self.includes = m.get('Includes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('ItemsDone') is not None:
            self.items_done = m.get('ItemsDone')

        if m.get('ItemsTotal') is not None:
            self.items_total = m.get('ItemsTotal')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')

        if m.get('RestoreName') is not None:
            self.restore_name = m.get('RestoreName')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        if m.get('SnapshotHash') is not None:
            self.snapshot_hash = m.get('SnapshotHash')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotVersion') is not None:
            self.snapshot_version = m.get('SnapshotVersion')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceClientId') is not None:
            self.source_client_id = m.get('SourceClientId')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        if m.get('VaultRegionId') is not None:
            self.vault_region_id = m.get('VaultRegionId')

        return self

class DescribeRestoreJobsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of restoration tasks returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **10**.
        self.page_size = page_size
        # The total number of restoration tasks returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

