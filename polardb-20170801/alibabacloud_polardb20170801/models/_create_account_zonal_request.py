# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountZonalRequest(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        account_privilege: str = None,
        account_type: str = None,
        client_token: str = None,
        dbcluster_id: str = None,
        dbname: str = None,
        node_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        priv_for_all_db: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.account_description = account_description
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.account_password = account_password
        self.account_privilege = account_privilege
        self.account_type = account_type
        self.client_token = client_token
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dbname = dbname
        self.node_type = node_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.priv_for_all_db = priv_for_all_db
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priv_for_all_db is not None:
            result['PrivForAllDB'] = self.priv_for_all_db

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivForAllDB') is not None:
            self.priv_for_all_db = m.get('PrivForAllDB')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

