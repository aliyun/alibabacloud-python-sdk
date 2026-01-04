# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddIPv6TranslatorAclListEntryRequest(DaraModel):
    def __init__(
        self,
        acl_entry_comment: str = None,
        acl_entry_ip: str = None,
        acl_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The remarks of the ACL entry.
        # 
        # It must be 2 to 100 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        self.acl_entry_comment = acl_entry_comment
        # The IPv6 address or IPv6 CIDR block that you want to add to the ACL entry, for example, 12XX:0:0:XXXX::0102 or 12XX:0:0:XXXX::/60.
        # 
        # This parameter is required.
        self.acl_entry_ip = acl_entry_ip
        # The ID of the ACL to which you want to add the IP entry.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the ACL.
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
        if self.acl_entry_comment is not None:
            result['AclEntryComment'] = self.acl_entry_comment

        if self.acl_entry_ip is not None:
            result['AclEntryIp'] = self.acl_entry_ip

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
        if m.get('AclEntryComment') is not None:
            self.acl_entry_comment = m.get('AclEntryComment')

        if m.get('AclEntryIp') is not None:
            self.acl_entry_ip = m.get('AclEntryIp')

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

