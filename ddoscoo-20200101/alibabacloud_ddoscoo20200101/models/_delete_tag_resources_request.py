# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteTagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the resource. Valid values:
        # 
        # - **true**
        # 
        # - **false** (default)
        self.all = all
        # The region ID of the Anti-DDoS instance. The value is fixed to **cn-hangzhou**, which indicates the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS instance belongs in Resource Management.
        # 
        # If you do not set this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # A list of IDs of the Anti-DDoS instances from which you want to remove tags.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The resource type. The value is fixed to **INSTANCE**, which indicates an Anti-DDoS instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # A list of tag keys to remove.
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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

