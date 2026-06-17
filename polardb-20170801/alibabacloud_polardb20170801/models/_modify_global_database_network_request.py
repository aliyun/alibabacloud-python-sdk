# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyGlobalDatabaseNetworkRequest(DaraModel):
    def __init__(
        self,
        enable_global_domain_name: bool = None,
        gdndescription: str = None,
        gdnid: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # Specifies whether to create a global domain name.
        self.enable_global_domain_name = enable_global_domain_name
        # The description of the GDN. It must meet the following requirements:
        # 
        # - Cannot start with http\\:// or https\\://.
        # 
        # - Must start with a letter or a Chinese character.
        # 
        # - Can contain letters, Chinese characters, digits, underscores (_), and hyphens (-).
        # 
        # - Must be 2 to 126 characters in length.
        self.gdndescription = gdndescription
        # The ID of the GDN.
        # 
        # This parameter is required.
        self.gdnid = gdnid
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_global_domain_name is not None:
            result['EnableGlobalDomainName'] = self.enable_global_domain_name

        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription

        if self.gdnid is not None:
            result['GDNId'] = self.gdnid

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableGlobalDomainName') is not None:
            self.enable_global_domain_name = m.get('EnableGlobalDomainName')

        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')

        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

