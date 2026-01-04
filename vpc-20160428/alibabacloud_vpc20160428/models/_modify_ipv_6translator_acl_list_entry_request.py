# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIPv6TranslatorAclListEntryRequest(DaraModel):
    def __init__(
        self,
        acl_entry_comment: str = None,
        acl_entry_id: str = None,
        acl_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The remarks of the ACL rule.
        # 
        # It must be 2 to 100 characters in length, and can contain digits, underscores (_), and hyphens (-). It must start with a letter.
        # 
        # This parameter is required.
        self.acl_entry_comment = acl_entry_comment
        # The ID of the ACL rule to which the IP entry belongs.
        # 
        # This parameter is required.
        self.acl_entry_id = acl_entry_id
        # The ID of the ACL to which the IP entry belongs.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region of the ACL.
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

        if self.acl_entry_id is not None:
            result['AclEntryId'] = self.acl_entry_id

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

        if m.get('AclEntryId') is not None:
            self.acl_entry_id = m.get('AclEntryId')

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

