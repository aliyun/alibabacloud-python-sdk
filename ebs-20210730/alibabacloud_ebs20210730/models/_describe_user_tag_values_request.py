# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserTagValuesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        tag_filter_value: str = None,
        tag_key: str = None,
    ):
        # Number of items per page in a paginated query. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 10, the default value is 10.
        # 
        # - If the set value is greater than 100, the default value is 100.
        self.max_results = max_results
        # Query token (Token). The value should be the NextToken parameter value from the previous call to this interface. This parameter is not required for the initial call. If NextToken is set, the PageSize and PageNumber request parameters become invalid, and the TotalCount in the response data is also invalid.
        self.next_token = next_token
        # The region ID of the consistency replication group.
        self.region_id = region_id
        # Tag content filter
        self.tag_filter_value = tag_filter_value
        # Tag key.
        self.tag_key = tag_key

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

        if self.tag_filter_value is not None:
            result['TagFilterValue'] = self.tag_filter_value

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TagFilterValue') is not None:
            self.tag_filter_value = m.get('TagFilterValue')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

