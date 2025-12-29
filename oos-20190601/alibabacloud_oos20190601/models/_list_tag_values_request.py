# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagValuesRequest(DaraModel):
    def __init__(
        self,
        key: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The tag key to query.
        self.key = key
        # The maximum number of results on each page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The type of the tagged resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

