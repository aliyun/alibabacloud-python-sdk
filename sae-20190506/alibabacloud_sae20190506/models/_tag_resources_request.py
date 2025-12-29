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
        # The IDs of resources. Separate multiple resource IDs with comma (,). This parameter is required if you do not specify the **Tags** parameter.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The type of the resource. Set the value to `application`.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag in the format of a key-value pair. This parameter is required if you do not specify the **ResourceIds** parameter. The following parameters are involved:
        # 
        # *   **key**: the tag key. It cannot exceed 128 characters in length.
        # *   **value**: the tag value. It cannot exceed 128 characters in length.
        # 
        # Tag keys and tag values are case-sensitive. If you specify multiple tags, the system adds all the tags to the specified resources. Each tag key on a resource can have only one tag value. If you create a tag that has the same key as an existing tag, the value of the existing tag is overwritten.
        # 
        # Tag keys and tag values cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

