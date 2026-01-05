# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupFilesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeBackupFilesResponseBodyData] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The backup files that are returned.
        self.data = data
        # The total number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request. If the request fails, provide this ID to technical support to assist in diagnosing the issue.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeBackupFilesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBackupFilesResponseBodyData(DaraModel):
    def __init__(
        self,
        android_instance_id: str = None,
        android_instance_name: str = None,
        backup_all: bool = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        backup_file_path: str = None,
        description: str = None,
        end_user_id: str = None,
        file_size: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        instance_group_id: str = None,
        region_id: str = None,
        source_app_info_list: List[str] = None,
        source_file_path_list: List[str] = None,
        status: str = None,
        system_version: str = None,
        task_id: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # The ID of the instance.
        self.android_instance_id = android_instance_id
        # The name of the instance.
        self.android_instance_name = android_instance_name
        # Indicates whether the whole instance is backed up.
        self.backup_all = backup_all
        # The ID of the backup file.
        self.backup_file_id = backup_file_id
        # The name of the backup file.
        self.backup_file_name = backup_file_name
        # The directory in which the backup file is stored.
        self.backup_file_path = backup_file_path
        # The description of the backup file.
        self.description = description
        # The owner of the backup file.
        self.end_user_id = end_user_id
        # The total size of the source files.
        self.file_size = file_size
        # The time when the backup file was created.
        self.gmt_created = gmt_created
        # The time when the backup file was last updated.
        self.gmt_modified = gmt_modified
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The region ID.
        self.region_id = region_id
        # The names of the application packages that are backed up.
        self.source_app_info_list = source_app_info_list
        # The directories of the source files.
        self.source_file_path_list = source_file_path_list
        # The status of the backup file.
        # 
        # Valid values:
        # 
        # *   AVAILABLE
        # *   RECOVERING
        self.status = status
        self.system_version = system_version
        # The task ID.
        self.task_id = task_id
        # The endpoint of the OSS bucket that stores the backup file.
        self.upload_endpoint = upload_endpoint
        # The type of the backup.
        # 
        # Valid values:
        # 
        # *   OSS: backup files are stored in OSS buckets. .
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id

        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name

        if self.backup_all is not None:
            result['BackupAll'] = self.backup_all

        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id

        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name

        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path

        if self.description is not None:
            result['Description'] = self.description

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_app_info_list is not None:
            result['SourceAppInfoList'] = self.source_app_info_list

        if self.source_file_path_list is not None:
            result['SourceFilePathList'] = self.source_file_path_list

        if self.status is not None:
            result['Status'] = self.status

        if self.system_version is not None:
            result['SystemVersion'] = self.system_version

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint

        if self.upload_type is not None:
            result['UploadType'] = self.upload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')

        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')

        if m.get('BackupAll') is not None:
            self.backup_all = m.get('BackupAll')

        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')

        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')

        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceAppInfoList') is not None:
            self.source_app_info_list = m.get('SourceAppInfoList')

        if m.get('SourceFilePathList') is not None:
            self.source_file_path_list = m.get('SourceFilePathList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        return self

