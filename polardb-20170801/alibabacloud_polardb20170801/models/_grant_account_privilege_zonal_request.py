# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantAccountPrivilegeZonalRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        client_token: str = None,
        dbcluster_id: str = None,
        dbname: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The privileges of the account. Valid values:
        # - ReadWrite: read and write
        # - ReadOnly: read-only
        # - DMLOnly: DML only
        # - DDLOnly: DDL only
        # - ReadIndex: read-only and index
        # 
        # This parameter is required.
        self.account_privilege = account_privilege
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must ensure that the token is unique among different requests. The token is case-sensitive and up to 64 ASCII characters in length.
        self.client_token = client_token
        # The ID of the PolarDB on ENS cluster. This operation applies only to edge clusters. For standard PolarDB clusters, use GrantAccountPrivilege. You can create an edge cluster by calling CreateDBCluster and setting CloudProvider to ENS and specifying EnsRegionId.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database to which privileges are granted. You can grant privileges to one or more databases at a time. Separate multiple database names with commas (,).
        # 
        # This parameter is required.
        self.dbname = dbname
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

