# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_arn: List[str] = None,
        resource_owner_account: str = None,
        tags: str = None,
    ):
        # The type of the tag. Valid values:
        # 
        # *   Custom
        # *   System
        # *   All
        # 
        # Default value: All.
        self.category = category
        # The token that is used to start the next query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of entries to return on each page.
        # 
        # Maximum value: 1000. Default value: 50.
        self.page_size = page_size
        # The region ID.
        # 
        # *   If the resources belong to a service that is centrally deployed, set the value to the region ID of the resources by referring to [Regions supported by tag-related operations on resources of centrally deployed Alibaba Cloud services](https://help.aliyun.com/document_detail/2579691.html).
        # *   If the resources belong to a service that is not centrally deployed, set the value to the region ID of the resources.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The Alibaba Cloud Resource Name (ARN) of a resource.
        # 
        # Valid values of N: 1 to 50.
        # 
        # ARN format: `arn:acs:${ProductCode}:${Region}:${Account}:${ResourceType}/${ResourceId}` Fields:
        # 
        # *   `ProductCode`: the service code. You can set this field to a value obtained from the response of the [ListSupportResourceTypes](https://help.aliyun.com/document_detail/2330915.html) operation.
        # *   `Region`: the region ID of the resource. You can set this field to an asterisk (\\*) to indicate the current region.
        # *   `Account`: the ID of the Alibaba Cloud account to which the resource belongs. You can set this field to an asterisk (\\*) to indicate the current Alibaba Cloud account.
        # *   `ResourceType`: the resource type. You can set this field to a value obtained from the response of the [ListSupportResourceTypes](https://help.aliyun.com/document_detail/2330915.html) operation.
        # *   `ResourceId`: the ID of the resource.
        # 
        # >  You can set `ProductCode` and `ResourceType` in ResourceARN to values defined in Resource Group, ActionTrail, or Resource Center.
        self.resource_arn = resource_arn
        self.resource_owner_account = resource_owner_account
        # The key-value pairs of tags. You can specify 1 to 10 key-value pairs.
        # 
        # If you specify multiple tags, the system queries the resources to which all these tags are added.
        # 
        # Limits:
        # 
        # *   A tag key must be 1 to 128 characters in length.
        # *   A tag value must be 1 to 128 characters in length.
        # *   Tag keys and tag values are case-sensitive.
        # *   Each tag key on a resource can have only one tag value. If you create a tag that has the same key as an existing tag, the value of the existing tag is overwritten.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

