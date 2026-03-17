# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeACLsRequest(DaraModel):
    def __init__(
        self,
        acl_ids: str = None,
        acl_type: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the ACL.
        # 
        # *   If you want to query multiple ACLs at the same time, separate the ACL IDs with commas (,).
        # *   If you do not set this parameter, all ACLs in the specified region are queried.
        self.acl_ids = acl_ids
        # The type of the SAG instance associated with the ACL. Valid values:
        # 
        # *   **acl-hardware**: SAG CPE instance
        # *   **acl-software**: SAG app instance
        self.acl_type = acl_type
        # The name of the ACL.
        # 
        # The name must be 2 to 100 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region where the ACL is deployed.
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
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.name is not None:
            result['Name'] = self.name

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
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

