# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVaultReplicationRegionsRequest(DaraModel):
    def __init__(
        self,
        token: str = None,
        vault_id: str = None,
    ):
        # This parameter is deprecated.
        self.token = token
        # This parameter is deprecated.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.token is not None:
            result['Token'] = self.token

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

