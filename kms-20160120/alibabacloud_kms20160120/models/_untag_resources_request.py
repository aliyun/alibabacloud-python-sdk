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
        # Specifies whether to remove all tags from resources. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # >  This parameter takes effect only when you specify an empty tag key.
        self.all = all
        # The region ID of the resource.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/601478.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources from which you want to remove tags. You can enter up to 50 resource IDs.
        # 
        # Enter multiple resource IDs in the `["ResourceId.1","ResourceId.2",...]` format.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource from which you want to remove tags. Valid values:
        # 
        # *   key
        # *   secret
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of the tags that you want to remove. You can enter up to 20 tag keys.
        # 
        # Enter multiple tag keys in the `["key.1","key.2",...]` format.
        # 
        # >  The tag key cannot start with aliyun or acs:.
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

