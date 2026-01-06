# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVaultRequest(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        token: str = None,
        vault_id: str = None,
    ):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The token.
        self.token = token
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.token is not None:
            result['Token'] = self.token

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

