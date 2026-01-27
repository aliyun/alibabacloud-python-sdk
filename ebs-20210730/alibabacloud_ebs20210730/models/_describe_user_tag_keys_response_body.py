# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUserTagKeysResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tag_keys: List[str] = None,
    ):
        # Number of items per page in paginated queries. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 10, the default is 10.
        # 
        # - If the set value is greater than 100, the default is 100.
        self.max_results = max_results
        # The token for the next query. An empty NextToken indicates there are no more results.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # List of matching tag keys.
        self.tag_keys = tag_keys

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

