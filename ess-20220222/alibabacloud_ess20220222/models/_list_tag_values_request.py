# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagValuesRequest(DaraModel):
    def __init__(
        self,
        key: str = None,
        next_token: str = None,
        owner_id: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        # The key of the tag.
        # 
        # This parameter is required.
        self.key = key
        # The token that determines the start point of the next query. If this parameter is empty, all results are returned.
        self.next_token = next_token
        self.owner_id = owner_id
        # The number of entries to return on each page. Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the Auto Scaling resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The type of the Auto Scaling resource. Set the value to scalinggroup. This indicates that the tag is added to a scaling group.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

