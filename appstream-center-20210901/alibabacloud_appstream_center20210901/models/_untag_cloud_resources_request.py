# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagCloudResourcesRequest(DaraModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tag_keys: List[str] = None,
    ):
        # The list of resource IDs. A maximum of 50 resource IDs are supported. This parameter is not required when the resource type is tenant ID.
        self.resource_ids = resource_ids
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tag keys. Both system tags and custom tags are supported. A maximum of 10 tag keys can be passed.
        # 
        # Valid values for system tags:
        # - `System/Scheduler/GRAYSCALE`: Canary release tag.
        # - `System/Scheduler/STOP_NEW_USER_CONNECTION`: Tag that prevents new users bound to the delivery group from establishing connections.
        # 
        # This parameter is required.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

