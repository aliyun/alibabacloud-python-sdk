# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAccessControlListEntryRequest(DaraModel):
    def __init__(
        self,
        acl_entrys: str = None,
        acl_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The configuration of the network ACL. Valid values:
        # 
        # *   **entry**: the IP entries that you want to add to the network ACL. You can add CIDR blocks. Separate multiple CIDR blocks with commas (,).
        # *   **comment**: the comment on the network ACL.
        # 
        # > You can add at most 50 IP entries to a network ACL in each call. If the IP entry that you want to add to a network ACL already exists, the IP entry is not added. The IP entries that you add must be CIDR blocks.
        self.acl_entrys = acl_entrys
        # The ID of the network ACL.
        self.acl_id = acl_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the network ACL.
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
        if self.acl_entrys is not None:
            result['AclEntrys'] = self.acl_entrys

        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntrys') is not None:
            self.acl_entrys = m.get('AclEntrys')

        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

