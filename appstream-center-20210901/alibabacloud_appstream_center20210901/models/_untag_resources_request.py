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
        # Specifies whether to remove all custom tags from the resources. **This parameter takes effect only when TagKey.N is not specified**. If TagKey.N is specified, this parameter is ignored. Valid values:
        # 
        # - true: Removes all custom tags from the resources, including Wuying system tags that start with `System/` and are bound by calling the [TagResources](~~TagResources~~) operation.
        # - false (default): Does not remove all tags. If TagKey.N is also not specified, the error code InvalidParameter.TagKeyListOrAll is returned.
        self.all = all
        # The region ID. This parameter is required. Set this parameter to the ID of the region where the app instance group resides, such as cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of resource IDs from which you want to remove tags. This parameter is required. Specify the app instance group IDs. A maximum of 50 IDs can be specified in a single request. Duplicate IDs are automatically deduplicated.
        # 
        # **All IDs must belong to existing app instance groups within the current Alibaba Cloud account.** If any ID does not exist or does not belong to the current account, the entire request fails and the error code InvalidAppInstanceGroup.NotFound is returned. No tags are removed from any resources.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. This parameter is required. **Currently, only app instance groups are supported**. The value is not case-sensitive, but we recommend that you use uppercase letters:
        # 
        # - APPINSTANCEGROUP: Wuying app instance group.
        # 
        # If you specify other values, the error code InvalidResourceType.Invalid is returned.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tag keys to be removed. A maximum of 20 tag keys can be specified in a single request. **You must specify at least one of TagKey.N and All**. If neither is specified, the error code InvalidParameter.TagKeyListOrAll is returned.
        # 
        # - If TagKey.N is specified, only the tags corresponding to these tag keys are removed, and the All parameter is ignored.
        # - If a specified tag key does not exist on a resource, the tag key is skipped and no error is returned.
        # - If TagKey.N is not specified, you must set All to true to remove all custom tags from the resources.
        # 
        # Tag keys that start with `System/` are Wuying system tags. Only the following values are supported:
        # 
        # - System/Scheduler/GRAYSCALE: The grayscale tag for the app instance group.
        # - System/Scheduler/STOP_NEW_USER_CONNECTION: Prevents new connections from users newly bound to the app instance group.
        # 
        # If you specify other tag keys that start with `System/`, the error code InvalidTagPolicy.KeyInvalid or InvalidTag.SystemKeyNotAllow is returned.
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

