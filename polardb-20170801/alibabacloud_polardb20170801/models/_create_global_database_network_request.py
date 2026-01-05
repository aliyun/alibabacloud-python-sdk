# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGlobalDatabaseNetworkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        enable_global_domain_name: bool = None,
        gdndescription: str = None,
        gdnversion: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the primary cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to create a global domain name.
        self.enable_global_domain_name = enable_global_domain_name
        # The description of the GDN. The description must meet the following requirements:
        # 
        # *   It cannot start with [http:// or https://.](http://https://。)
        # *   It must start with a letter.
        # *   It can contain letters, digits, underscores (_), and hyphens (-).
        # *   It must be 2 to 126 characters in length.
        self.gdndescription = gdndescription
        self.gdnversion = gdnversion
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_global_domain_name is not None:
            result['EnableGlobalDomainName'] = self.enable_global_domain_name

        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription

        if self.gdnversion is not None:
            result['GDNVersion'] = self.gdnversion

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
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableGlobalDomainName') is not None:
            self.enable_global_domain_name = m.get('EnableGlobalDomainName')

        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')

        if m.get('GDNVersion') is not None:
            self.gdnversion = m.get('GDNVersion')

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

