# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tags: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The resource IDs. You can specify up to 50 resource IDs in a JSON array. This parameter is required unless you specify the **Tags** parameter.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The resource type. Only `application` is supported.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key-value pairs of the tags. This parameter is required unless you specify the **ResourceIds** parameter. The following rules apply:
        # 
        # - **key**: The tag key. The key must be 1 to 128 characters in length.
        # 
        # - **value**: The tag value. The value must be 1 to 128 characters in length.
        # 
        # Tags are case-sensitive. If you specify multiple tags, they are created and bound to the specified resources. For a single resource, each tag key must be unique. If you specify a tag key that already exists for a resource, the operation updates the existing tag value.
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

