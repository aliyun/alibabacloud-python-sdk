# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_owner_account: str = None,
        resource_type: str = None,
        tags: List[main_models.ListTagResourcesRequestTags] = None,
    ):
        # The token that determines the start point of the next query.
        self.next_token = next_token
        self.owner_id = owner_id
        # The region ID of the resource. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/2679950.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the Auto Scaling resources. You can specify 1 to 50 resource IDs.
        self.resource_ids = resource_ids
        self.resource_owner_account = resource_owner_account
        # The resource type. Set the value to scalinggroup.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # Details of the tags.
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListTagResourcesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The key is used to perform an exact match of Auto Scaling resources. The key must be 1 to 128 characters in length.
        # 
        # `Tags` is used to perform an exact match of Auto Scaling resources to which the specified tags are added. Specify a tag in the key-value pair format.
        # 
        # *   If you specify only `Tags.Key`, all resources whose tags contain the specified tag key are returned.
        # *   If you specify only `Tags.Value`, the `MissingParameter.TagKey` error is reported.
        # *   If you specify multiple key-value pairs at the same time, only Auto Scaling resources that match all the tag keys and tag values are returned.
        self.key = key
        # The value of the tag. The value is used to perform an exact match of Auto Scaling resources. The value can be up to 128 characters in length.
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

