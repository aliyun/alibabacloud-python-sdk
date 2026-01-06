# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVaultRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        resource_group_id: str = None,
        vault_id: str = None,
        vault_name: str = None,
        worm_enabled: bool = None,
    ):
        # The description of the backup vault. The description must be 0 to 255 characters in length.
        self.description = description
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id
        # The name of the backup vault. The name must be 1 to 64 characters in length.
        self.vault_name = vault_name
        # Specifies whether to enable the immutable backup feature for storage vaults. After the immutable backup feature is enabled, backup vaults and all backup data cannot be deleted until the retention period expires. The immutable backup feature cannot be disabled after it is enabled. Only standard backup vaults and archive vaults support the immutable backup feature.
        self.worm_enabled = worm_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        if self.vault_name is not None:
            result['VaultName'] = self.vault_name

        if self.worm_enabled is not None:
            result['WormEnabled'] = self.worm_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        if m.get('VaultName') is not None:
            self.vault_name = m.get('VaultName')

        if m.get('WormEnabled') is not None:
            self.worm_enabled = m.get('WormEnabled')

        return self

