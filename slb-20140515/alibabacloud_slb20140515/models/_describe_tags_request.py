# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTagsRequest(DaraModel):
    def __init__(
        self,
        distinct_key: bool = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: str = None,
    ):
        # Specifies whether the tags contain distinct keys.
        # 
        # Valid values: true and false.
        self.distinct_key = distinct_key
        # The SLB instance ID.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 50. Maximum value: 100.
        self.page_size = page_size
        # The region ID of the Server Load Balancer (SLB) instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags that you want to query.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distinct_key is not None:
            result['DistinctKey'] = self.distinct_key

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistinctKey') is not None:
            self.distinct_key = m.get('DistinctKey')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

