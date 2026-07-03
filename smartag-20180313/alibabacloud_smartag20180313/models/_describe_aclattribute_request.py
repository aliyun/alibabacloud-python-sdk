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
        # The ID of the access control list (ACL) instance.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The direction of the access control rule. Valid values:
        # 
        # - **in**: inbound. Refers to traffic from external sources accessing the local branch where the Smart Access Gateway (SAG) instance is deployed.
        # - **out**: outbound. Refers to traffic from the local branch where the SAG instance is deployed accessing external destinations.
        self.direction = direction
        # The name of the ACL instance.
        # 
        # The name must be 2 to 100 characters in length and must start with an uppercase letter, a lowercase letter, or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        # > This parameter supports fuzzy search.
        self.name = name
        # The order ID.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number in a paginated query. Default value: **1**.
        self.page_number = page_number
        # The number of access control rule entries to display per page in a paginated query.
        # 
        # Valid values: **1** to **50**.
        # 
        # Default value: **10**.
        self.page_size = page_size
        # The region ID of the access control list (ACL) instance.
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

