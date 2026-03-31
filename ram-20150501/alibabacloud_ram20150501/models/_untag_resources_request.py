# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        resource_names: List[str] = None,
        resource_type: str = None,
        tag_keys: List[str] = None,
    ):
        # Specifies whether to remove all tags from the resources.
        # 
        # Enumerated values:
        # 
        # *   true
        # *   false
        self.all = all
        # The names of the resources. You can specify up to 50 resource names.
        self.resource_names = resource_names
        # The resource type.
        # 
        # Enumerated values:
        # 
        # *   role: RAM roles.
        # *   policy: policies.
        self.resource_type = resource_type
        # The keys of the tags. You can specify up to 20 tag keys.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.resource_names is not None:
            result['ResourceNames'] = self.resource_names

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ResourceNames') is not None:
            self.resource_names = m.get('ResourceNames')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

