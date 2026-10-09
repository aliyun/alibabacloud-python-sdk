# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSupabaseBackupJobsRequest(DaraModel):
    def __init__(
        self,
        backup_mode: str = None,
        max_results: int = None,
        next_token: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # The backup mode. Valid values:
        # 
        # - Automated: automatic backup
        # - Manual: manual backup
        # 
        # If this parameter is not specified, all backup tasks are returned.
        self.backup_mode = backup_mode
        # The maximum number of entries to return for this request.
        self.max_results = max_results
        # The paging token. Do not specify this parameter for the first query. For subsequent queries, specify the NextToken value returned in the previous response.
        self.next_token = next_token
        # Instance ID of the Supabase instance. You can obtain instance ID from the Supabase page in the console.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query available region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

