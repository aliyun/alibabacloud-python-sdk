# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeACLAttributeRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        direction: str = None,
        name: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the access control instance.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The direction in which the access control rule is applied. Valid values:
        # 
        # - **in**: inbound, which indicates traffic from external networks to the local branch where the Smart Access Gateway instance is deployed.
        # - **out**: outbound, which indicates traffic from the local branch where the Smart Access Gateway instance is deployed to external networks.
        self.direction = direction
        # The name of the access control instance.
        # 
        # The name must be 2 to 100 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). It must start with a letter or Chinese character.
        # > Fuzzy search is supported for this parameter.
        self.name = name
        # The order ID.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number for a paging query. Default value: **1**.
        self.page_number = page_number
        # The number of access control rule entries to return on each page in a paging query.
        # 
        # Valid values: **1** to **50**.
        # 
        # Default value: **10**.
        self.page_size = page_size
        # The region ID of the access control instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

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

        return self

