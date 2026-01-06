# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the file system.
        # 
        # This parameter is valid only if the TagKey.N parameter is not specified.
        # 
        # Valid values:
        # 
        # *   true: All tags are removed from the file system. If the file system does not have tags, a success message is returned.
        # *   false (default): No tags are removed from the file system and a success message is returned.
        self.all = all
        # The resource IDs. Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # Set the value to filesystem.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys of the resources. Valid values of N: 1 to 20.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

