# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        directory_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags. This parameter takes effect only when the list of tag keys is empty.
        self.all = all
        # The directory ID.
        self.directory_id = directory_id
        # The list of resource IDs. You can specify up to 50 resource IDs in a single call.
        # > 
        # > - Supported resource types include users and access configurations:
        # > - - If the resource type is user, specify the user ID.
        # > - - If the resource type is access configuration, specify the access configuration ID.
        # 
        # <notice>If the DirectoryId parameter is not specified, you must add the prefix "${DirectoryId}_" to the resource ID.</notice>
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Users and access configurations are supported. Valid values:
        # - user: user
        # - accessConfiguration: access configuration
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tag keys. You can specify up to 20 tag keys in a single call.
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

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

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

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

