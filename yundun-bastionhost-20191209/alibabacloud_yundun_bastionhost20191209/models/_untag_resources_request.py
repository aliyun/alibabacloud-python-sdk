# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the Bastionhost instance.
        # 
        # - If you specify \\`TagKey.N\\`, you must set \\`All\\` to **false** to remove specific tags.
        # 
        # - If you do not specify \\`TagKey.N\\`, set \\`All\\` to **true** to remove all tags. If you set \\`All\\` to **false**, no tags are removed.
        self.all = all
        # The ID of the region where the Bastionhost instance resides.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the instance.
        # 
        # The value of N can be from 1 to 20.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the ID of the Bastionhost instance.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # The only valid value is **INSTANCE**. This value indicates a Bastionhost instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key of the tag.
        # 
        # The value of N can be from 1 to 20.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

