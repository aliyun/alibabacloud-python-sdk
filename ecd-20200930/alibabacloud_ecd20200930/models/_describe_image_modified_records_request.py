# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageModifiedRecordsRequest(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The cloud desktop ID.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # Number of entries per page for paged queries.
        # 
        # - Maximum: 100.
        # 
        # - Default: 10.
        self.max_results = max_results
        # Pagination token. Set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # Region ID. Call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to list regions that support WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

