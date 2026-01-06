# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateRamPolicyRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        require_base_policy: bool = None,
        resource_group_id: str = None,
        vault_id: str = None,
    ):
        # The type of policy that you want to generate. Valid values:
        # 
        # *   BACKUP: the permission to back up data to a backup vault
        # *   RESTORE: the permission to restore data from a backup vault
        # 
        # This parameter is required.
        self.action_type = action_type
        # Specifies whether to generate the policy based on an existing instance-specific rule. Valid values:
        # 
        # *   true
        # *   false
        self.require_base_policy = require_base_policy
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.require_base_policy is not None:
            result['RequireBasePolicy'] = self.require_base_policy

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('RequireBasePolicy') is not None:
            self.require_base_policy = m.get('RequireBasePolicy')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

