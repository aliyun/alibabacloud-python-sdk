# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDomainRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dkim_selector: str = None,
    ):
        # Domain name, length 1-50, can include numbers, uppercase letters, lowercase letters, ., and -.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The selector field in the DKIM protocol, used to identify a specific public key. It is recommended to leave it blank, as the system will automatically generate it based on cluster information. If the user specifies it manually, for example, if the sending domain is "sub.example.com" and dkimSelector is set to "default", then the host record will be "default._domainkey.sub"
        # Constraints: 
        # 1. The length must not exceed 60 characters. 
        # 2. It must consist of visible characters only. 
        # 3. It cannot start with a hyphen (-). 
        # 4. It cannot end with a hyphen (-). 
        # 5. It cannot contain any of the following characters: _ :;/!*~.@#$%^&()+=[{]}|?<>,\\""
        self.dkim_selector = dkim_selector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.dkim_selector is not None:
            result['dkimSelector'] = self.dkim_selector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('dkimSelector') is not None:
            self.dkim_selector = m.get('dkimSelector')

        return self

