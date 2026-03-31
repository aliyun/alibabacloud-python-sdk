# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        resource_names_shrink: str = None,
        resource_type: str = None,
        tag_keys_shrink: str = None,
    ):
        # Specifies whether to remove all tags from the resources.
        # 
        # Enumerated values:
        # 
        # *   true
        # *   false
        self.all = all
        # The names of the resources. You can specify up to 50 resource names.
        self.resource_names_shrink = resource_names_shrink
        # The resource type.
        # 
        # Enumerated values:
        # 
        # *   role: RAM roles.
        # *   policy: policies.
        self.resource_type = resource_type
        # The keys of the tags. You can specify up to 20 tag keys.
        self.tag_keys_shrink = tag_keys_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.resource_names_shrink is not None:
            result['ResourceNames'] = self.resource_names_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ResourceNames') is not None:
            self.resource_names_shrink = m.get('ResourceNames')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')

        return self

