# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDirectoriesRequest(DaraModel):
    def __init__(
        self,
        directory_id: List[str] = None,
        directory_status: str = None,
        directory_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The directory IDs. You can specify one or more directory IDs.
        self.directory_id = directory_id
        # The directory status. This parameter is the same as Status.
        self.directory_status = directory_status
        # The directory type.
        self.directory_type = directory_type
        # The number of entries per page in a paged query.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token for the next query. An empty value indicates that no more results exist.
        self.next_token = next_token
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The directory status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_status is not None:
            result['DirectoryStatus'] = self.directory_status

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryStatus') is not None:
            self.directory_status = m.get('DirectoryStatus')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

