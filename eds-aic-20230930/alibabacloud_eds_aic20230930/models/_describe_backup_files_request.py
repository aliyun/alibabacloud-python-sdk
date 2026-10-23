# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeBackupFilesRequest(DaraModel):
    def __init__(
        self,
        android_instance_id: str = None,
        android_instance_name: str = None,
        backup_all: bool = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        description: str = None,
        end_time: str = None,
        end_user_id: str = None,
        instance_group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        sale_mode: str = None,
        start_time: str = None,
        status_list: List[str] = None,
    ):
        # The instance ID.
        self.android_instance_id = android_instance_id
        # The name of the instance. Fuzzy match is supported.
        self.android_instance_name = android_instance_name
        # Specifies whether the backup is a full device backup.
        self.backup_all = backup_all
        # The ID of the backup file.
        self.backup_file_id = backup_file_id
        # The name of the backup file. Fuzzy match is supported.
        self.backup_file_name = backup_file_name
        # The description. Fuzzy match is supported.
        self.description = description
        # The end time to query backup files. Specify the time in the YYYY-MM-DD HH:mm:ss format.
        self.end_time = end_time
        # The owner of the backup file.
        self.end_user_id = end_user_id
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # The maximum number of entries to return per page in a paging query. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token that specifies the starting position of the query. An empty value indicates that the query starts from the beginning.
        self.next_token = next_token
        # The sales mode. Instance indicates the cloud phone instance mode, and Node indicates the cloud phone matrix mode.
        self.sale_mode = sale_mode
        # The start time to query backup files. Specify the time in the YYYY-MM-DD HH:mm:ss format.
        self.start_time = start_time
        # The list of backup file statuses.
        self.status_list = status_list

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

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_list is not None:
            result['StatusList'] = self.status_list

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

