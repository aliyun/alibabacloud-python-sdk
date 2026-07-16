# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_arn: List[str] = None,
        resource_owner_account: str = None,
        tags: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # *   If the resources belong to a service that is centrally deployed, set the value to `cn-hangzhou` or to the region ID of the resources by referring to [Regions supported by tag-related operations on resources of centrally deployed Alibaba Cloud services](https://help.aliyun.com/document_detail/2579691.html).
        # *   If the resources belong to a service that is not centrally deployed, set the value to the region ID of the resources.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The Alibaba Cloud Resource Name (ARN) of a resource.
        # 
        # This parameter is required.
        self.resource_arn = resource_arn
        self.resource_owner_account = resource_owner_account
        # The key-value pairs of tags. You can specify 1 to 10 key-value pairs.
        # 
        # If you specify multiple tags, the system adds all the tags to the specified resources.
        # 
        # Limits:
        # 
        # *   A tag key must be 1 to 128 characters in length.
        # *   A tag value must be 1 to 128 characters in length.
        # *   Tag keys and tag values are case-sensitive.
        # *   Each tag key on a resource can have only one tag value. If you create a tag that has the same key as an existing tag, the value of the existing tag is overwritten.
        # 
        # This parameter is required.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

