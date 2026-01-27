# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserTagKeysRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        tag_filter_key: str = None,
    ):
        # Number of items per page in paginated queries. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 10, the default is 10.
        # 
        # - If the set value is greater than 100, the default is 100.
        self.max_results = max_results
        # The query token returned by this call (Token).
        self.next_token = next_token
        # The ID of the region to which the resource belongs. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest list of Alibaba Cloud regions.
        self.region_id = region_id
        # The tagKey for filtering the query.
        self.tag_filter_key = tag_filter_key

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

        if self.tag_filter_key is not None:
            result['TagFilterKey'] = self.tag_filter_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TagFilterKey') is not None:
            self.tag_filter_key = m.get('TagFilterKey')

        return self

