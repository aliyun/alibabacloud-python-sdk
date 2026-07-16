# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGraphicAuthSchemeConfigRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        platform: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_name: str = None,
    ):
        self.owner_id = owner_id
        self.platform = platform
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_name = scheme_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')

        return self

