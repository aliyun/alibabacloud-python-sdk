# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSupabaseDataBackupsRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_mode: str = None,
        backup_status: str = None,
        data_type: str = None,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the backup set. You can obtain the ID from the BackupSetId parameter returned by the ListSupabaseDataBackups operation.
        self.backup_id = backup_id
        # The backup pattern. Valid values: Automated: automatic backup. Manual: manual backup.
        self.backup_mode = backup_mode
        # The status of the backup set. Valid values: Success: the backup is successful; Failed: the backup fails.
        self.backup_status = backup_status
        # The backup type. Valid values: DATA: full backup; RESTOREPOI: restorable point.
        self.data_type = data_type
        # The end time of the query. The end time must be later than the start time. Format: yyyy-MM-ddTHH:mmZ (UTC).
        self.end_time = end_time
        # The maximum number of entries to return for the current request.
        self.max_results = max_results
        # The paging token for paged query. Do not specify this parameter for the first request. For subsequent requests, specify the NextToken value returned by the previous response.
        self.next_token = next_token
        # The page number. The value must be greater than 0 and cannot exceed the maximum value of an integer. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - 30
        # - 50
        # - 100
        # 
        # Default value: 30.
        self.page_size = page_size
        # Instance ID of the Supabase instance. You can obtain instance ID from the Supabase page in the console.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query available region IDs.
        self.region_id = region_id
        # The start time of the query. Format: yyyy-MM-ddTHH:mmZ (UTC).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

