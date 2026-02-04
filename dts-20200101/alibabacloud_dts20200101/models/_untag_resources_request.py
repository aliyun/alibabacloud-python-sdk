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
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to unbind all tags from the specified instances. Valid values:
        # 
        # *   **true**: unbinds all tags from the specified instances.
        # *   **false**: To unbind only specific tags, you must specify the **TagKey.N** parameter.
        # 
        # > 
        # *   You must specify at least one of the All and **TagKey.N** parameters.
        # *   If you specify both the All parameter and the **TagKey.N** parameter, the All parameter does not take effect.
        self.all = all
        # The ID of the region where the data migration, data synchronization, or change tracking instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the data migration, synchronization, and subscription instances, which can be queried by calling the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) API. > N indicates the Nth instance ID to be passed. For example, ResourceId.0 represents passing the first instance ID; ResourceId.1 represents passing the second instance ID. You can unbind tags for 1 to 50 instances simultaneously.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid value: **ALIYUN::DTS::INSTANCE**.
        self.resource_type = resource_type
        # Tag key. > - N indicates the position of the tag key being passed. For example, TagKey.0 represents the first tag key; TagKey.1 represents the second tag key. Up to 20 tag keys can be unbound simultaneously. - Empty strings are not allowed. - At least one of **All** or this parameter must be provided. - If both **All** and this parameter are provided, only this parameter will take effect.
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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

