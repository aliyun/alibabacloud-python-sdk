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
        # Specifies whether to remove instance tags from the instance. Valid values:
        # 
        # - **true**: yes. Removes instance tags from the instance.
        # - **false**: no. You must specify the tags to be removed in the **TagKey.N** parameter.
        # 
        # > - You must specify at least one of the **TagKey.N** parameter and this parameter.
        # - If you specify both the **TagKey.N** parameter and this parameter, this parameter does not take effect.
        self.all = all
        # The region ID. Specify this parameter to indicate the region where the instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The IDs of the data migration, data synchronization, and change tracking instances. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance IDs.
        # > N specifies the sequence number of the instance ID. For example, ResourceId.0 specifies the first instance ID, and ResourceId.1 specifies the second instance ID. You can remove tags from 1 to 50 instances at a time.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid value: **ALIYUN::DTS::INSTANCE**.
        self.resource_type = resource_type
        # The tag key.
        # > - N specifies the sequence number of the tag key. For example, TagKey.0 specifies the first tag key, and TagKey.1 specifies the second tag key. You can remove 1 to 20 tag keys at a time.
        # - Empty strings are not allowed.
        # - You must specify at least one of the **All** parameter and this parameter.
        # - If you specify both the **All** parameter and this parameter, only this parameter takes effect.
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

