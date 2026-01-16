# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReceiverRequest(DaraModel):
    def __init__(
        self,
        desc: str = None,
        owner_id: int = None,
        receivers_alias: str = None,
        receivers_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # List description.
        self.desc = desc
        self.owner_id = owner_id
        # List alias, an email address less than 30 characters long.
        # 
        # This parameter is required.
        self.receivers_alias = receivers_alias
        # List name, must be unique, with a length of 1-30 characters.
        # 
        # This parameter is required.
        self.receivers_name = receivers_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.receivers_alias is not None:
            result['ReceiversAlias'] = self.receivers_alias

        if self.receivers_name is not None:
            result['ReceiversName'] = self.receivers_name

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReceiversAlias') is not None:
            self.receivers_alias = m.get('ReceiversAlias')

        if m.get('ReceiversName') is not None:
            self.receivers_name = m.get('ReceiversName')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

