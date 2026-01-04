# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListServerGroupServersRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        server_group_id: str = None,
        server_ids: List[str] = None,
        server_ips: List[str] = None,
    ):
        # The number of entries to return in each call. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The pagination token used to specify a particular page of results. Valid values:
        # 
        # *   Left this parameter empty if this is the first query or the only query.
        # *   Set this parameter to the value of NextToken obtained from the previous query.
        self.next_token = next_token
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The IDs of the backend servers. You can specify up to 40 backend servers in each call.
        self.server_ids = server_ids
        # The IP addresses of the backend servers. You can specify up to 40 backend servers in each call.
        self.server_ips = server_ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.server_ids is not None:
            result['ServerIds'] = self.server_ids

        if self.server_ips is not None:
            result['ServerIps'] = self.server_ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('ServerIds') is not None:
            self.server_ids = m.get('ServerIds')

        if m.get('ServerIps') is not None:
            self.server_ips = m.get('ServerIps')

        return self

