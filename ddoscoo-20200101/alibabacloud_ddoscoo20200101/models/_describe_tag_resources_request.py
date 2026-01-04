# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[main_models.DescribeTagResourcesRequestTags] = None,
    ):
        # The query token. Set the value to the value of **NextToken** that is returned in the last call.
        # 
        # > You do not need to configure this parameter if you call this operation for the first time.
        self.next_token = next_token
        # The region ID of the instance. Set the value to **cn-hangzhou**, which indicates an Anti-DDoS Proxy (Chinese Mainland) instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not configure this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The IDs of the Anti-DDoS Proxy (Chinese Mainland) instances that you want to query.
        self.resource_ids = resource_ids
        # The type of the resource to which the tag belongs. Set the value to **INSTANCE**, which indicates an Anti-DDoS Pro instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # An array consisting of tags that you want to query. Each tag consists of a tag **key** and a tag **value**.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeTagResourcesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that you want to query.
        # 
        # > 
        # 
        # *   You must specify at least one of the **ResourceIds.N** and **Tags.N.Key** parameters.
        # 
        # *   You can call the [DescribeTagKeys](https://help.aliyun.com/document_detail/159785.html) operation to query all tag keys.
        self.key = key
        # The value of the tag that you want to query.
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

