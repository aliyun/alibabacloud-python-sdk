# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        # A query can return a maximum of 50 results. If the number of results exceeds this limit, the response includes a NextToken. To retrieve the next page of results, pass this token in your next request.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs, specified as a JSON array of strings. This parameter is required if the **Tags** parameter is not specified.
        self.resource_ids = resource_ids
        # The resource type. Only `application` is supported.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags used to filter resources. This parameter is required if the **ResourceIds** parameter is not specified. A tag is a key-value pair.
        # 
        # - **key**: The tag key. The key can be 1 to 128 characters in length.
        # 
        # - **value**: The tag value. The value can be 1 to 128 characters in length.
        # 
        # Tag keys and tag values are case-sensitive. If you specify multiple tags, the operation returns only resources that have all the specified tags.
        # 
        # A tag key cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

