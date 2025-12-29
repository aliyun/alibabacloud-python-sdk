# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySrvNetworkAddressRequest(DaraModel):
    def __init__(
        self,
        connection_type: str = None,
        dbinstance_id: str = None,
        new_connection_string: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.connection_type = connection_type
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.new_connection_string = new_connection_string
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
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.new_connection_string is not None:
            result['NewConnectionString'] = self.new_connection_string

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
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NewConnectionString') is not None:
            self.new_connection_string = m.get('NewConnectionString')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

