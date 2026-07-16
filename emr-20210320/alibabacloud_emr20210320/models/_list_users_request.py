# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        user_name: str = None,
        user_names: List[str] = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The maximum number of entries to return.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The username. Fuzzy match is supported.
        self.user_name = user_name
        # The usernames. Number of elements in the array: 0 to 20.
        self.user_names = user_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_names is not None:
            result['UserNames'] = self.user_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')

        return self

