# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudDriveUsersRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The ID of the enterprise network drive.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The end user ID.
        # 
        # If specified, the query returns only the personal drive of that user. If left empty, the query returns the personal drives of all users.
        self.end_user_id = end_user_id
        # The number of entries per page.
        # 
        # - Maximum: 100.
        # 
        # - Default: 10.
        self.max_results = max_results
        # The token for the next page of results. This is the `NextToken` value from the previous response. Leave this parameter empty for the first request.
        self.next_token = next_token
        # The region ID. To obtain a list of supported regions, call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html).
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
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

