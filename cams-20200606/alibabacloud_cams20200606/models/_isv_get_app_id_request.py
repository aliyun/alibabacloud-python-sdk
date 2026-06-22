# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IsvGetAppIdRequest(DaraModel):
    def __init__(
        self,
        intl_version: str = None,
        owner_id: int = None,
        permissions: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        type: str = None,
    ):
        self.intl_version = intl_version
        self.owner_id = owner_id
        self.permissions = permissions
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intl_version is not None:
            result['IntlVersion'] = self.intl_version

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.permissions is not None:
            result['Permissions'] = self.permissions

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntlVersion') is not None:
            self.intl_version = m.get('IntlVersion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

