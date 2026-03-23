# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePostgresExtensionsRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        client_token: str = None,
        dbinstance_id: str = None,
        dbnames: str = None,
        extensions: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        risk_confirmed: bool = None,
        source_database: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        self.client_token = client_token
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.dbnames = dbnames
        self.extensions = extensions
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.risk_confirmed = risk_confirmed
        self.source_database = source_database

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbnames is not None:
            result['DBNames'] = self.dbnames

        if self.extensions is not None:
            result['Extensions'] = self.extensions

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

        if self.risk_confirmed is not None:
            result['RiskConfirmed'] = self.risk_confirmed

        if self.source_database is not None:
            result['SourceDatabase'] = self.source_database

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBNames') is not None:
            self.dbnames = m.get('DBNames')

        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')

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

        if m.get('RiskConfirmed') is not None:
            self.risk_confirmed = m.get('RiskConfirmed')

        if m.get('SourceDatabase') is not None:
            self.source_database = m.get('SourceDatabase')

        return self

