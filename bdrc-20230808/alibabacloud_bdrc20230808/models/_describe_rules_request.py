# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRulesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_category_id: str = None,
        resource_owner_ids: List[int] = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The number of entries to return on each page. Maximum value: 50. Default value: 10.
        self.max_results = max_results
        # The token to retrieve the next page of results. You can obtain this token from the `NextToken` parameter in the previous response.
        self.next_token = next_token
        # The resource category ID.
        self.resource_category_id = resource_category_id
        self.resource_owner_ids = resource_owner_ids
        # The ID of the region where the resource resides.
        self.resource_region_id = resource_region_id
        # The resource type.
        self.resource_type = resource_type

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

        if self.resource_category_id is not None:
            result['ResourceCategoryId'] = self.resource_category_id

        if self.resource_owner_ids is not None:
            result['ResourceOwnerIds'] = self.resource_owner_ids

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        if m.get('ResourceOwnerIds') is not None:
            self.resource_owner_ids = m.get('ResourceOwnerIds')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

