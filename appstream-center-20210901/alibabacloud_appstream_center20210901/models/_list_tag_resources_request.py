# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.ListTagResourcesRequestTag] = None,
    ):
        # The paged query token. You do not need to specify this parameter for the first request. If the previous invoke returned a non-empty NextToken value, pass it in as-is to retrieve subsequent paging results.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of resource IDs. A maximum of 50 resource IDs are supported.
        # 
        # If the resource type is delivery group, specify the delivery group ID (prefixed with `aig-`). You can call the ListAppInstanceGroup operation to obtain the delivery group ID.
        # 
        # > Specify at least one of ResourceId.N and Tag.N. If only ResourceId.N is specified, all tags bound to the specified resources are returned.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - APPINSTANCEGROUP: delivery group.
        # 
        # This parameter is case-insensitive. Only this value is supported. If you specify other values, the error code `InvalidResourceType.Invalid` is returned.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tag conditions. A maximum of 20 tag conditions are supported.
        # 
        # > Specify at least one of ResourceId.N and Tag.N. Multiple tags have an AND relationship. Only resources that have all specified tags bound are returned.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListTagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. This parameter is required. The tag key is case-sensitive and must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. The tag value is case-sensitive and can be up to 256 characters in length. If this parameter is not specified, the value of the tag key is not restricted, which means any tag value under the key is matched.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

